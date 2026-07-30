<script lang="ts">
	import { page } from '$app/state';
	import { buttonVariants } from '$lib/components/ui/button';
	import ThemeToggle from '$lib/components/theme-toggle.svelte';

	const links = [
		{ href: '/', label: 'Recherche' },
		{ href: '/pinned', label: 'Épinglés' },
		{ href: '/analytics', label: 'Analyses' }
	];
</script>

<div class="flex items-center justify-between">
	<h1 class="text-lg font-semibold">Twitter Datum</h1>
	<nav class="flex items-center gap-1">
		{#each links as link (link.href)}
			<a
				href={link.href}
				class={buttonVariants({
					variant: page.url.pathname === link.href ? 'secondary' : 'ghost',
					size: 'sm'
				})}
			>
				{link.label}
			</a>
		{/each}
		<ThemeToggle />
	</nav>
</div>
