<script lang="ts">
	import { page } from '$app/state';
	import { resolve } from '$app/paths';
	import { SvelteURLSearchParams } from 'svelte/reactivity';
	import { categoryStyle, formatCompact } from '$lib/categories';
	import ThemeToggle from '$lib/components/theme-toggle.svelte';
	import type { Facet } from '$lib/types';

	let { categories }: { categories: Facet[] } = $props();

	const links = [
		{ href: resolve('/'), label: 'Recherche' },
		{ href: resolve('/pinned'), label: 'Épinglés' },
		{ href: resolve('/analytics'), label: 'Analyses' }
	];

	const total = $derived(categories.reduce((sum, c) => sum + c.count, 0));
	const activeCategory = $derived(
		page.url.pathname === '/' ? page.url.searchParams.get('category') : null
	);

	function categoryHref(value: string) {
		const params =
			page.url.pathname === '/'
				? new SvelteURLSearchParams(page.url.searchParams)
				: new SvelteURLSearchParams();
		params.delete('page');
		if (activeCategory === value) {
			params.delete('category');
		} else {
			params.set('category', value);
		}
		const qs = params.toString();
		return qs ? `${resolve('/')}?${qs}` : resolve('/');
	}
</script>

<aside
	class="flex flex-col gap-7 bg-[#14171F] px-5 py-7 text-[#E8E6E1] md:sticky md:top-0 md:h-screen"
>
	<div class="flex items-center gap-2.5">
		<span class="size-2.5 shrink-0 rounded-full bg-[#7FB8A6] shadow-[0_0_0_3px_rgba(127,184,166,0.25)]"
		></span>
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
		</div>
		<div class="flex flex-col gap-1.5">
			{#each categories as c (c.value)}
				{@const style = categoryStyle(c.value!)}
				{@const active = activeCategory === c.value}
				<a
					href={categoryHref(c.value!)}
					class="flex items-center gap-2.5 rounded-lg px-2 py-1.5 hover:bg-white/5 {active
						? 'bg-white/[0.07]'
						: ''}"
				>
					<span class="size-2.5 shrink-0 rounded-sm {style.dot}"></span>
					<span class="flex-1 text-[12.5px] text-[#D6D8DE]">{c.value}</span>
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
</aside>
