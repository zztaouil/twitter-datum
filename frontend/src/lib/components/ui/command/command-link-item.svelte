<script lang="ts">
	import { Command as CommandPrimitive } from 'bits-ui';
	import CheckIcon from '@lucide/svelte/icons/check';
	import { cn } from '$lib/utils.js';

	let {
		ref = $bindable(null),
		class: className,
		selected = false,
		children,
		...restProps
	}: CommandPrimitive.LinkItemProps & { selected?: boolean } = $props();
</script>

<CommandPrimitive.LinkItem
	bind:ref
	data-slot="command-item"
	class={cn(
		'relative flex cursor-default items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-hidden select-none data-selected:bg-accent data-selected:text-accent-foreground',
		className
	)}
	{...restProps}
>
	<span class="flex size-4 items-center justify-center">
		{#if selected}
			<CheckIcon />
		{/if}
	</span>
	{@render children?.()}
</CommandPrimitive.LinkItem>
