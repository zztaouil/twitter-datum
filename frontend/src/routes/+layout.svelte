<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.png';
	import NavBar from '$lib/components/nav-bar.svelte';
	import { setPlotDefaults } from 'svelteplot';

	setPlotDefaults({ locale: 'fr-FR' });

	let { children } = $props();
</script>

<svelte:head><link rel="icon" href={favicon} /></svelte:head>
<div class="mx-auto flex max-w-2xl flex-col gap-4 p-6">
	<NavBar />
	{@render children()}
</div>
