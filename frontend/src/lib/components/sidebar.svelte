<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/state';
	import { resolve } from '$app/paths';
	import { SvelteURLSearchParams } from 'svelte/reactivity';
	import { categoryStyle, categoryLabel, formatCompact } from '$lib/categories';
	import ThemeToggle from '$lib/components/theme-toggle.svelte';
	import { RangeCalendar } from '$lib/components/ui/range-calendar';
	import * as Popover from '$lib/components/ui/popover';
	import * as Command from '$lib/components/ui/command';
	import { Badge } from '$lib/components/ui/badge';
	import { parseDate } from '@internationalized/date';
	import type { DateRange } from 'bits-ui';
	import type { Facet } from '$lib/types';
	import ChevronsUpDown from '@lucide/svelte/icons/chevrons-up-down';
	import X from '@lucide/svelte/icons/x';

	let { categories, authors }: { categories: Facet[]; authors: Facet[] } = $props();

	function currentParams() {
		return page.url.pathname === '/'
			? new SvelteURLSearchParams(page.url.searchParams)
			: new SvelteURLSearchParams();
	}

	const links = [
		{ href: resolve('/'), label: 'Recherche' },
		{ href: resolve('/pinned'), label: 'Épinglés' },
		{ href: resolve('/analytics'), label: 'Analyses' }
	];

	const total = $derived(categories.reduce((sum, c) => sum + c.count, 0));
	const activeCategories = $derived(
		page.url.pathname === '/' ? page.url.searchParams.getAll('category') : []
	);

	// each selected category matches tweets classified as exactly that category —
	// picking several is an OR (any exact match), not tweets combining several aspects
	function categoryHref(value: string) {
		const params = currentParams();
		params.delete('page');
		params.delete('category');
		const next = activeCategories.includes(value)
			? activeCategories.filter((c) => c !== value)
			: [...activeCategories, value];
		for (const c of next) params.append('category', c);
		const qs = params.toString();
		return qs ? `${resolve('/')}?${qs}` : resolve('/');
	}

	const activeAuthors = $derived(
		page.url.pathname === '/' ? page.url.searchParams.getAll('author') : []
	);

	function authorHref(username: string) {
		const params = currentParams();
		params.delete('page');
		params.delete('author');
		const next = activeAuthors.includes(username)
			? activeAuthors.filter((a) => a !== username)
			: [...activeAuthors, username];
		for (const a of next) params.append('author', a);
		const qs = params.toString();
		return qs ? `${resolve('/')}?${qs}` : resolve('/');
	}

	let dateRange = $state<DateRange>({ start: undefined, end: undefined });
	$effect(() => {
		const from = page.url.pathname === '/' ? page.url.searchParams.get('from') : null;
		const to = page.url.pathname === '/' ? page.url.searchParams.get('to') : null;
		dateRange = { start: from ? parseDate(from) : undefined, end: to ? parseDate(to) : undefined };
	});

	function applyDateRange() {
		const params = currentParams();
		params.delete('page');
		if (dateRange.start) params.set('from', dateRange.start.toString());
		else params.delete('from');
		if (dateRange.end) params.set('to', dateRange.end.toString());
		else params.delete('to');
		const qs = params.toString();
		goto(qs ? `${resolve('/')}?${qs}` : resolve('/'), {
			keepFocus: true,
			noScroll: true,
			replaceState: true
		});
	}
</script>

<aside
	class="flex flex-col gap-7 bg-[#14171F] px-5 py-7 text-[#E8E6E1] md:sticky md:top-0 md:h-screen"
>
	<div class="flex items-center gap-2.5">
		<!-- <span
			class="size-2.5 shrink-0 rounded-full bg-[#7FB8A6] shadow-[0_0_0_3px_rgba(127,184,166,0.25)]"
		></span> -->
		<div class="flex-1">
			<span class="text-sm font-bold">Twitter Datum</span>
			<div class="font-mono text-[10.5px] tracking-wide text-[#8B8E98]">
				{formatCompact(total)} TWEETS INDEXÉS
			</div>
		</div>
		<ThemeToggle
			class="size-8 border-white/10 bg-transparent text-[#C7C9D1] hover:bg-white/10 hover:text-white"
		/>
	</div>

	<nav class="flex flex-col gap-0.5">
		{#each links as link (link.href)}
			<a
				href={link.href}
				class="flex items-center justify-between rounded-md px-2.5 py-2 text-sm font-medium text-[#C7C9D1] hover:bg-white/5 {page
					.url.pathname === link.href
					? 'bg-[#1D212B] text-white'
					: ''}"
			>
				{link.label}
				{#if link.href === '/'}
					<span class="font-mono text-[11px] text-[#7A7D87]">{formatCompact(total)}</span>
				{/if}
			</a>
		{/each}
	</nav>

	<div>
		<div class="mb-2.5 text-[10.5px] font-semibold tracking-wide text-[#797C86] uppercase">
			Catégories
			{#if activeCategories.length > 1}
				<span class="normal-case text-[#8B8E98]">· combinées</span>
			{/if}
		</div>
		<div class="flex flex-col gap-1.5">
			{#each categories as c (c.value)}
				{@const style = categoryStyle(c.value!)}
				{@const active = activeCategories.includes(c.value!)}
				<a
					href={categoryHref(c.value!)}
					class="flex items-center gap-2.5 rounded-lg px-2 py-1.5 hover:bg-white/5 {active
						? 'bg-white/[0.07]'
						: ''}"
				>
					<span class="size-2.5 shrink-0 rounded-sm {style.dot}"></span>
					<span class="flex-1 text-[12.5px] text-[#D6D8DE]">{categoryLabel(c.value!)}</span>
					<span class="font-mono text-[10.5px] text-[#8B8E98]">{formatCompact(c.count)}</span>
				</a>
			{/each}
		</div>
		<div class="mt-1.5 h-0.75 overflow-hidden rounded-full bg-[#2A2E3A]">
			<div class="flex h-full">
				{#each categories as c (c.value)}
					<div
						class="h-full {categoryStyle(c.value!).bar}"
						style="width: {total ? (c.count / total) * 100 : 0}%"
					></div>
				{/each}
			</div>
		</div>
	</div>

	<div>
		<div class="mb-2.5 text-[10.5px] font-semibold tracking-wide text-[#797C86] uppercase">
			Auteurs
		</div>
		<Popover.Root>
			<Popover.Trigger
				class="flex w-full items-center justify-between rounded-lg border border-white/10 bg-white/5 px-2.5 py-1.5 text-[12.5px] text-[#D6D8DE] hover:bg-white/10"
			>
				<span class="truncate">
					{activeAuthors.length
						? `${activeAuthors.length} sélectionné${activeAuthors.length > 1 ? 's' : ''}`
						: 'Tous les auteurs'}
				</span>
				<ChevronsUpDown class="size-3.5 shrink-0 opacity-60" />
			</Popover.Trigger>
			<Popover.Content
				class="w-64 p-0 [--accent-foreground:#E8E6E1] [--accent:rgba(255,255,255,0.07)] [--border:rgba(255,255,255,0.1)] [--foreground:#E8E6E1] [--muted-foreground:#8B8E98] [--popover-foreground:#E8E6E1] [--popover:#14171F]"
				align="start"
			>
				<Command.Root>
					<Command.Input placeholder="Rechercher un auteur…" />
					<Command.List>
						<Command.Empty>Aucun auteur trouvé.</Command.Empty>
						<Command.Group>
							{#each authors as a (a.username)}
								{@const active = activeAuthors.includes(a.username!)}
								<Command.LinkItem
									href={authorHref(a.username!)}
									selected={active}
									value={a.username}
								>
									<span class="flex-1 truncate">@{a.username}</span>
									<span class="font-mono text-xs text-muted-foreground"
										>{formatCompact(a.count)}</span
									>
								</Command.LinkItem>
							{/each}
						</Command.Group>
					</Command.List>
				</Command.Root>
			</Popover.Content>
		</Popover.Root>
		{#if activeAuthors.length}
			<div class="mt-1.5 flex flex-wrap gap-1">
				{#each activeAuthors as username (username)}
					<Badge href={authorHref(username)} variant="secondary" class="gap-1">
						@{username}
						<X class="size-3" />
					</Badge>
				{/each}
			</div>
		{/if}
	</div>

	<div>
		<div class="mb-2.5 flex items-center justify-between">
			<span class="text-[10.5px] font-semibold tracking-wide text-[#797C86] uppercase">Dates</span>
			{#if dateRange.start}
				<button
					type="button"
					class="text-[10.5px] text-[#8B8E98] hover:text-white"
					onclick={() => {
						dateRange = { start: undefined, end: undefined };
						applyDateRange();
					}}
				>
					Effacer
				</button>
			{/if}
		</div>
		<RangeCalendar
			bind:value={dateRange}
			onValueChange={applyDateRange}
			locale="fr-FR"
			class="w-full rounded-lg border border-white/10 bg-white/3 [--cell-size:--spacing(7)]"
		/>
	</div>
</aside>
