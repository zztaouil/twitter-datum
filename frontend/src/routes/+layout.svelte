<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.svg';
	import NavBar from '$lib/components/nav-bar.svelte';

	let { children } = $props();
</script>

<svelte:head><link rel="icon" href={favicon} /></svelte:head>
<div class="mx-auto flex max-w-2xl flex-col gap-4 p-6">
	<NavBar />
	{@render children()}
</div>
