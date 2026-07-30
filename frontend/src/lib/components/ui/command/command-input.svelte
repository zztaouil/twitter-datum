<script lang="ts">
	import { Command as CommandPrimitive } from 'bits-ui';
	import SearchIcon from '@lucide/svelte/icons/search';
	import { cn } from '$lib/utils.js';

	let {
		ref = $bindable(null),
		value = $bindable(''),
		class: className,
		...restProps
	}: CommandPrimitive.InputProps = $props();
</script>

<div data-slot="command-input-wrapper" class="flex items-center gap-2 border-b px-3">
	<SearchIcon class="size-4 shrink-0 opacity-50" />
	<CommandPrimitive.Input
		bind:ref
		bind:value
		data-slot="command-input"
		class={cn(
			'flex h-9 w-full rounded-md bg-transparent py-3 text-sm outline-hidden placeholder:text-muted-foreground disabled:cursor-not-allowed disabled:opacity-50',
			className
		)}
		{...restProps}
	/>
</div>
