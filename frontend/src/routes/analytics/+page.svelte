<script lang="ts">
	import { Plot, BarX, RuleX, setPlotDefaults } from 'svelteplot';
	import { Skeleton } from '$lib/components/ui/skeleton';
	import type {
		CategoryComboStat,
		CoverageStat,
		MediaBackfillStat,
		ReplyDepthStat,
		TargetAnalytics
	} from '$lib/types';
	import type { PageData } from './$types';
	import { categoryLabel, comboLabel, COMBO_COLORS } from '$lib/categories';

	let { data }: { data: PageData } = $props();
	setPlotDefaults({ locale: 'fr-FR' });
	let visible = $state([false, false, false, false, false]);

	function revealWhenNear(node: HTMLElement, index: number) {
		if (!('IntersectionObserver' in window)) {
			visible[index] = true;
			return;
		}

		const observer = new IntersectionObserver(
			(entries) => {
				if (entries.some((entry) => entry.isIntersecting)) {
					visible[index] = true;
					observer.disconnect();
				}
			},
			{ rootMargin: '200px' }
		);
		observer.observe(node);
		return { destroy: () => observer.disconnect() };
	}

	const barHeight = (n: number) => n * 18 + 60;

	// floating hover tooltip shared by any chart that passes a `detail` field on its rows
	let tooltip = $state<{ x: number; y: number; text: string } | null>(null);
	const showTooltip = (e: Event, d: { detail: string }) => {
		const { clientX, clientY } = e as PointerEvent;
		tooltip = { x: clientX, y: clientY, text: d.detail };
	};
	const hideTooltip = () => {
		tooltip = null;
	};

	// section 1 — category-combination breakdown (a multi-category tweet counts once for
	// its exact combo, not once per category); hover a bar for the full per-target detail
	const combosByTotal = (targets: CategoryComboStat[]) =>
		[...targets].filter((t) => t.total > 0).sort((a, b) => b.total - a.total);
	const comboRows = (targets: CategoryComboStat[]) =>
		combosByTotal(targets).flatMap((t) => {
			const present = t.combos
				.filter((c) => c.count > 0 && c.value !== 'unclassified')
				.sort((a, b) => b.count - a.count);
			const total = present.reduce((sum, c) => sum + c.count, 0);
			const detail = [
				`${t.username} — ${total} tweets classés`,
				...present.map(
					(c) => `${comboLabel(c.value!)} : ${c.count} (${((c.count / total) * 100).toFixed(1)}%)`
				)
			].join('\n');
			return present.map((c) => ({
				username: t.username,
				combo: comboLabel(c.value!),
				count: c.count,
				detail
			}));
		});

	// section 1b — category distribution (100% stacked, biggest targets first)
	const targetsByTotal = (targets: TargetAnalytics[]) =>
		[...targets].filter((t) => t.total > 0).sort((a, b) => b.total - a.total);
	// "unclassified" is excluded everywhere below — it's not a real category, just noise
	const categoryRows = (targets: TargetAnalytics[]) =>
		targetsByTotal(targets).flatMap((t) =>
			t.categories
				.filter((c) => c.count > 0 && c.value !== 'unclassified')
				.map((c) => ({ username: t.username, category: categoryLabel(c.value!), count: c.count }))
		);

	// section 2 — collection coverage: % of profile tweets_count actually collected
	const coverageSorted = (rows: CoverageStat[]) =>
		[...rows].filter((c) => c.tweets_count > 0).sort((a, b) => b.pct - a.pct);

	// section 3 — media_type backfill progress, least-done first (highlights what's pending)
	const mediaSorted = (rows: MediaBackfillStat[]) =>
		[...rows].filter((m) => m.total > 0).sort((a, b) => a.pct - b.pct);

	// section 4 — reply-graph depth, ordered by level-1 replies per tweet
	const replyDepthSorted = (rows: ReplyDepthStat[]) =>
		[...rows].filter((r) => r.tweets > 0).sort((a, b) => b.l1_per_tweet - a.l1_per_tweet);
</script>

<h1 class="text-xl font-bold">Analyses</h1>

<div class="flex flex-col gap-10">
	<div class="flex flex-col gap-4" use:revealWhenNear={0}>
		<h2 class="text-sm font-medium">Combinaisons de catégories par cible</h2>
		<p class="text-xs text-muted-foreground">survolez une colonne pour le détail par combinaison</p>
		{#if !visible[0]}
			<Skeleton class="h-64 w-full" />
		{:else}
			{#await data.combos}
				<Skeleton class="h-64 w-full" />
			{:then combos}
				{@const targets = combosByTotal(combos.results)}
				<Plot
					y={{ domain: targets.map((t) => t.username) }}
					x={{ percent: true, label: '% des tweets classés' }}
					color={{
						legend: true,
						domain: Object.keys(COMBO_COLORS).map(comboLabel),
						range: Object.values(COMBO_COLORS)
					}}
					height={barHeight(targets.length)}
				>
					<BarX
						data={comboRows(combos.results)}
						y="username"
						x="count"
						fill="combo"
						stack={{ offset: 'normalize', order: null, reverse: false }}
						onpointerenter={showTooltip}
						onpointermove={showTooltip}
						onpointerleave={hideTooltip}
					/>
				</Plot>
			{/await}
		{/if}
	</div>

	<div class="flex flex-col gap-4" use:revealWhenNear={1}>
		<h2 class="text-sm font-medium">Répartition par catégorie</h2>
		{#if !visible[1]}
			<Skeleton class="h-64 w-full" />
		{:else}
			{#await data.analytics}
				<Skeleton class="h-64 w-full" />
			{:then analytics}
				{@const targets = targetsByTotal(analytics.targets)}
				<Plot
					y={{ domain: targets.map((t) => t.username) }}
					x={{ percent: true, label: '% des tweets' }}
					color={{ legend: true }}
					height={barHeight(targets.length)}
				>
					<BarX
						data={categoryRows(analytics.targets)}
						y="username"
						x="count"
						fill="category"
						stack={{ offset: 'normalize', order: null, reverse: false }}
					/>
				</Plot>
			{/await}
		{/if}
	</div>

	<div class="flex flex-col gap-4" use:revealWhenNear={2}>
		<h2 class="text-sm font-medium">Couverture de la collecte</h2>
		<p class="text-xs text-muted-foreground">
			% des tweets du profil réellement collectés, par cible
		</p>
		{#if !visible[2]}
			<Skeleton class="h-64 w-full" />
		{:else}
			{#await data.coverage}
				<Skeleton class="h-64 w-full" />
			{:then coverage}
				{@const rows = coverageSorted(coverage.results)}
				<Plot
					y={{ domain: rows.map((c) => c.username) }}
					x={{ domain: [0, 100], label: '% collecté' }}
					height={barHeight(rows.length)}
				>
					<RuleX data={[0]} />
					<BarX data={rows} y="username" x="pct" fill="var(--color-chart-1)" />
				</Plot>
			{/await}
		{/if}
	</div>

	<div class="flex flex-col gap-4" use:revealWhenNear={3}>
		<h2 class="text-sm font-medium">Rétro-remplissage des médias</h2>
		<p class="text-xs text-muted-foreground">
			% des tweets avec un type de média renseigné (le moins avancé en premier)
		</p>
		{#if !visible[3]}
			<Skeleton class="h-64 w-full" />
		{:else}
			{#await data.media}
				<Skeleton class="h-64 w-full" />
			{:then media}
				{@const rows = mediaSorted(media.results)}
				<Plot
					y={{ domain: rows.map((m) => m.username) }}
					x={{ domain: [0, 100], label: '% renseigné' }}
					height={barHeight(rows.length)}
				>
					<RuleX data={[0]} />
					<BarX data={rows} y="username" x="pct" fill="var(--color-chart-2)" />
				</Plot>
			{/await}
		{/if}
	</div>

	<div class="flex flex-col gap-4" use:revealWhenNear={4}>
		<h2 class="text-sm font-medium">Profondeur des réponses</h2>
		<p class="text-xs text-muted-foreground">
			réponses de niveau 1 et niveau 2 par tweet, triées par niveau 1
		</p>
		{#if !visible[4]}
			<div class="grid grid-cols-2 gap-4">
				<Skeleton class="h-64 w-full" />
				<Skeleton class="h-64 w-full" />
			</div>
		{:else}
			{#await data.replyDepth}
				<div class="grid grid-cols-2 gap-4">
					<Skeleton class="h-64 w-full" />
					<Skeleton class="h-64 w-full" />
				</div>
			{:then replyDepth}
				{@const rows = replyDepthSorted(replyDepth.results)}
				{@const domain = rows.map((r) => r.username)}
				<div class="grid grid-cols-2 gap-4">
					<Plot
						y={{ domain, axis: 'left' }}
						x={{ label: 'réponses N1 / tweet' }}
						height={barHeight(domain.length)}
					>
						<RuleX data={[0]} />
						<BarX data={rows} y="username" x="l1_per_tweet" fill="var(--color-chart-3)" />
					</Plot>
					<Plot
						y={{ domain, axis: false }}
						x={{ label: 'réponses N2 / tweet' }}
						height={barHeight(domain.length)}
					>
						<RuleX data={[0]} />
						<BarX data={rows} y="username" x="l2_per_tweet" fill="var(--color-chart-4)" />
					</Plot>
				</div>
			{/await}
		{/if}
	</div>
</div>

{#if tooltip}
	<div
		class="pointer-events-none fixed z-50 rounded-md border bg-popover px-2 py-1.5 text-xs whitespace-pre-line text-popover-foreground shadow-md"
		style="left: {tooltip.x + 12}px; top: {tooltip.y + 12}px;"
	>
		{tooltip.text}
	</div>
{/if}
