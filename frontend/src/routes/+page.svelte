<script lang="ts">
	import { mockTweets } from '$lib/mock-tweets';
	import { Input } from '$lib/components/ui/input';
	import { Badge } from '$lib/components/ui/badge';
	import * as Select from '$lib/components/ui/select';
	import * as Card from '$lib/components/ui/card';
	import * as Avatar from '$lib/components/ui/avatar';
	import * as Popover from '$lib/components/ui/popover';
	import { RangeCalendar } from '$lib/components/ui/range-calendar';
	import { Button, buttonVariants } from '$lib/components/ui/button';
	import { DateFormatter, getLocalTimeZone } from '@internationalized/date';
	import type { DateRange } from 'bits-ui';
	import X from '@lucide/svelte/icons/x';
	import ThemeToggle from '$lib/components/theme-toggle.svelte';

	const categories = [...new Set(mockTweets.map((t) => t.category))].sort();
	const df = new DateFormatter('en-US', { dateStyle: 'medium' });

	let query = $state('');
	let category = $state('all');
	let dateRange = $state<DateRange>({ start: undefined, end: undefined });

	const from = $derived(dateRange.start?.toString() ?? '');
	const to = $derived(dateRange.end?.toString() ?? '');

	const rangeLabel = $derived.by(() => {
		if (!dateRange.start) return 'All dates';
		const start = df.format(dateRange.start.toDate(getLocalTimeZone()));
		if (!dateRange.end) return start;
		return `${start} – ${df.format(dateRange.end.toDate(getLocalTimeZone()))}`;
	});

	const filtered = $derived(
		mockTweets.filter((t) => {
			if (category !== 'all' && t.category !== category) return false;
			if (from && t.created_at < from) return false;
			if (to && t.created_at > to + 'T23:59:59') return false;
			if (query) {
				const q = query.toLowerCase();
				const haystack = `${t.text} ${t.username} ${t.fullname}`.toLowerCase();
				if (!haystack.includes(q)) return false;
			}
			return true;
		})
	);

	function formatDate(iso: string) {
		return new Date(iso).toLocaleDateString(undefined, {
			year: 'numeric',
			month: 'short',
			day: 'numeric'
		});
	}
</script>

<div class="mx-auto flex max-w-2xl flex-col gap-4 p-6">
	<div class="flex items-center justify-between">
		<h1 class="text-lg font-semibold">Twitter Datum</h1>
		<ThemeToggle />
	</div>

	<div class="flex flex-col gap-2 rounded-lg border p-3">
		<Input placeholder="Search by content or author…" bind:value={query} />
		<div class="flex flex-wrap gap-2">
			<Select.Root type="single" bind:value={category}>
				<Select.Trigger class="w-48">
					{category === 'all' ? 'All categories' : category}
				</Select.Trigger>
				<Select.Content>
					<Select.Item value="all">All categories</Select.Item>
					{#each categories as c (c)}
						<Select.Item value={c}>{c}</Select.Item>
					{/each}
				</Select.Content>
			</Select.Root>
			<div class="flex items-center gap-1">
				<Popover.Root>
					<Popover.Trigger class={buttonVariants({ variant: 'outline', class: 'font-normal' })}>
						{rangeLabel}
					</Popover.Trigger>
					<Popover.Content class="w-auto p-0" align="start">
						<RangeCalendar bind:value={dateRange} />
					</Popover.Content>
				</Popover.Root>
				{#if dateRange.start}
					<Button
						variant="ghost"
						size="icon"
						aria-label="Clear dates"
						onclick={() => (dateRange = { start: undefined, end: undefined })}
					>
						<X class="size-4" />
					</Button>
				{/if}
			</div>
		</div>
	</div>

	<p class="text-muted-foreground text-sm">{filtered.length} tweets</p>

	<div class="flex flex-col gap-3">
		{#each filtered as tweet (tweet.id)}
			<Card.Root>
				<Card.Header>
					<div class="flex items-center gap-3">
						<Avatar.Root>
							<Avatar.Fallback>{tweet.username[0]?.toUpperCase()}</Avatar.Fallback>
						</Avatar.Root>
						<div class="flex flex-1 flex-col">
							<span class="font-medium">{tweet.fullname}</span>
							<span class="text-muted-foreground text-sm">@{tweet.username}</span>
						</div>
						<div class="flex flex-col items-end gap-1">
							<Badge variant="secondary">{tweet.category}</Badge>
							<span class="text-muted-foreground text-xs">{formatDate(tweet.created_at)}</span>
						</div>
					</div>
				</Card.Header>
				<Card.Content>
					<p class="whitespace-pre-wrap">{tweet.text}</p>
				</Card.Content>
			</Card.Root>
		{:else}
			<p class="text-muted-foreground py-8 text-center">No tweets match your filters.</p>
		{/each}
	</div>
</div>
