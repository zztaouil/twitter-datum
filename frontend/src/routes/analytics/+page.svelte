<script lang="ts">
	import { Plot, BarX, RuleX } from 'svelteplot';
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();

	const barHeight = (n: number) => n * 18 + 60;

	// section 1 — category distribution (100% stacked, biggest targets first)
	const targetsByTotal = $derived(
		[...data.targets].filter((t) => t.total > 0).sort((a, b) => b.total - a.total)
	);
	const categoryRows = $derived(
		targetsByTotal.flatMap((t) =>
			t.categories.filter((c) => c.count > 0).map((c) => ({ username: t.username, category: c.value, count: c.count }))
		)
	);
	const categoryDomain = $derived(targetsByTotal.map((t) => t.username));

	// section 2 — collection coverage: % of profile tweets_count actually collected
	const coverageSorted = $derived([...data.coverage].filter((c) => c.tweets_count > 0).sort((a, b) => b.pct - a.pct));

	// section 3 — media_type backfill progress, least-done first (highlights what's pending)
	const mediaSorted = $derived([...data.media].filter((m) => m.total > 0).sort((a, b) => a.pct - b.pct));

	// section 4 — reply-graph depth, ordered by level-1 replies per tweet
	const replyDepthSorted = $derived([...data.replyDepth].filter((r) => r.tweets > 0).sort((a, b) => b.l1_per_tweet - a.l1_per_tweet));
	const replyDepthDomain = $derived(replyDepthSorted.map((r) => r.username));
</script>

<div class="flex flex-col gap-10">
	<div class="flex flex-col gap-4">
		<h2 class="text-sm font-medium">Répartition par catégorie</h2>
		<Plot
			y={{ domain: categoryDomain }}
			x={{ percent: true, label: '% des tweets' }}
			color={{ legend: true }}
			height={barHeight(categoryDomain.length)}
		>
			<BarX
				data={categoryRows}
				y="username"
				x="count"
				fill="category"
				stack={{ offset: 'normalize', order: null, reverse: false }}
			/>
		</Plot>
	</div>

	<div class="flex flex-col gap-4">
		<h2 class="text-sm font-medium">Couverture de la collecte</h2>
		<p class="text-muted-foreground text-xs">% des tweets du profil réellement collectés, par cible</p>
		<Plot
			y={{ domain: coverageSorted.map((c) => c.username) }}
			x={{ domain: [0, 100], label: '% collecté' }}
			height={barHeight(coverageSorted.length)}
		>
			<RuleX data={[0]} />
			<BarX data={coverageSorted} y="username" x="pct" fill="var(--color-chart-1)" />
		</Plot>
	</div>

	<div class="flex flex-col gap-4">
		<h2 class="text-sm font-medium">Rétro-remplissage des médias</h2>
		<p class="text-muted-foreground text-xs">% des tweets avec un type de média renseigné (le moins avancé en premier)</p>
		<Plot
			y={{ domain: mediaSorted.map((m) => m.username) }}
			x={{ domain: [0, 100], label: '% renseigné' }}
			height={barHeight(mediaSorted.length)}
		>
			<RuleX data={[0]} />
			<BarX data={mediaSorted} y="username" x="pct" fill="var(--color-chart-2)" />
		</Plot>
	</div>

	<div class="flex flex-col gap-4">
		<h2 class="text-sm font-medium">Profondeur des réponses</h2>
		<p class="text-muted-foreground text-xs">réponses de niveau 1 et niveau 2 par tweet, triées par niveau 1</p>
		<div class="grid grid-cols-2 gap-4">
			<Plot y={{ domain: replyDepthDomain, axis: 'left' }} x={{ label: 'réponses N1 / tweet' }} height={barHeight(replyDepthDomain.length)}>
				<RuleX data={[0]} />
				<BarX data={replyDepthSorted} y="username" x="l1_per_tweet" fill="var(--color-chart-3)" />
			</Plot>
			<Plot y={{ domain: replyDepthDomain, axis: false }} x={{ label: 'réponses N2 / tweet' }} height={barHeight(replyDepthDomain.length)}>
				<RuleX data={[0]} />
				<BarX data={replyDepthSorted} y="username" x="l2_per_tweet" fill="var(--color-chart-4)" />
			</Plot>
		</div>
	</div>
</div>
