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
	}: CommandPrimitive.ItemProps & { selected?: boolean } = $props();
</script>

<CommandPrimitive.Item
	bind:ref
	data-slot="command-item"
	class={cn(
		"relative flex cursor-default items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-hidden select-none data-selected:bg-accent data-selected:text-accent-foreground data-[disabled=true]:pointer-events-none data-[disabled=true]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
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
</CommandPrimitive.Item>
