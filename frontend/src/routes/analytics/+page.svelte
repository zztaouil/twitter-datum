<script lang="ts">
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();

	const colors = ['bg-chart-1', 'bg-chart-2', 'bg-chart-3', 'bg-chart-4', 'bg-chart-5'];
	const targets = $derived([...data.targets].filter((t) => t.total > 0).sort((a, b) => b.total - a.total));
</script>

<div class="flex flex-col gap-4">
	<h2 class="text-sm font-medium">Category distribution by target</h2>

	<div class="flex flex-wrap gap-3 text-xs">
		{#each data.categories as category, i (category)}
			<span class="flex items-center gap-1">
				<span class="{colors[i % colors.length]} size-2.5 rounded-full"></span>
				{category}
			</span>
		{/each}
	</div>

	<div class="flex flex-col gap-3">
		{#each targets as target (target.username)}
			<div class="flex flex-col gap-1">
				<div class="flex items-center justify-between text-sm">
					<span class="font-medium">@{target.username}</span>
					<span class="text-muted-foreground text-xs">{target.total}</span>
				</div>
				<div class="bg-muted flex h-3 overflow-hidden rounded-full">
					{#each target.categories as c, i (c.value)}
						{#if c.count > 0}
							<div
								class={colors[i % colors.length]}
								style="width: {(c.count / target.total) * 100}%"
								title="{c.value}: {c.count}"
							></div>
						{/if}
					{/each}
				</div>
			</div>
		{:else}
			<p class="text-muted-foreground py-8 text-center text-sm">No classified tweets yet.</p>
		{/each}
	</div>
</div>
