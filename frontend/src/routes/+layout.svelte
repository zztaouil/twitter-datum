<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.png';
	import Sidebar from '$lib/components/sidebar.svelte';
	import { setPlotDefaults } from 'svelteplot';
	import type { Snippet } from 'svelte';
	import type { LayoutData } from './$types';

	setPlotDefaults({ locale: 'fr-FR' });

	let { data, children }: { data: LayoutData; children: Snippet } = $props();
</script>

<svelte:head><link rel="icon" href={favicon} /></svelte:head>
<div class="grid min-h-screen grid-cols-1 md:grid-cols-[268px_1fr]">
	<Sidebar categories={data.categories} />
	<main class="flex flex-col gap-4 p-6 md:p-8">
		{@render children()}
	</main>
</div>
