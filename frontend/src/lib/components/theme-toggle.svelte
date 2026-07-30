<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import Sun from '@lucide/svelte/icons/sun';
	import Moon from '@lucide/svelte/icons/moon';

	let { class: className = '' }: { class?: string } = $props();

	let dark = $state(typeof document !== 'undefined' && document.documentElement.classList.contains('dark'));

	function toggle() {
		dark = !dark;
		document.documentElement.classList.toggle('dark', dark);
		localStorage.setItem('theme', dark ? 'dark' : 'light');
	}
</script>

<Button variant="outline" size="icon" class={className} onclick={toggle} aria-label="Changer de thème">
	{#if dark}
		<Sun class="size-4" />
	{:else}
		<Moon class="size-4" />
	{/if}
</Button>
