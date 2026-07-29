<script lang="ts">
	import { goto } from '$app/navigation';
	import { navigating } from '$app/state';
	import { Input } from '$lib/components/ui/input';
	import { Badge } from '$lib/components/ui/badge';
	import * as Select from '$lib/components/ui/select';
	import * as Card from '$lib/components/ui/card';
	import * as Avatar from '$lib/components/ui/avatar';
	import * as Popover from '$lib/components/ui/popover';
	import { RangeCalendar } from '$lib/components/ui/range-calendar';
	import { Button, buttonVariants } from '$lib/components/ui/button';
	import { DateFormatter, getLocalTimeZone, parseDate } from '@internationalized/date';
	import type { DateRange } from 'bits-ui';
	import X from '@lucide/svelte/icons/x';
	import ThemeToggle from '$lib/components/theme-toggle.svelte';
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();

	const df = new DateFormatter('en-US', { dateStyle: 'medium' });

	let query = $state(data.filters.q);
	let category = $state(data.filters.category || 'all');
	let author = $state(data.filters.author || 'all');
	let dateRange = $state<DateRange>({
		start: data.filters.from ? parseDate(data.filters.from) : undefined,
		end: data.filters.to ? parseDate(data.filters.to) : undefined
	});

	// keep controls in sync with back/forward navigation, which changes `data` without going through applyFilters
	$effect(() => {
		query = data.filters.q;
		category = data.filters.category || 'all';
		author = data.filters.author || 'all';
		dateRange = {
			start: data.filters.from ? parseDate(data.filters.from) : undefined,
			end: data.filters.to ? parseDate(data.filters.to) : undefined
		};
	});

	const rangeLabel = $derived.by(() => {
		if (!dateRange.start) return 'All dates';
		const start = df.format(dateRange.start.toDate(getLocalTimeZone()));
		if (!dateRange.end) return start;
		return `${start} – ${df.format(dateRange.end.toDate(getLocalTimeZone()))}`;
	});

	function applyFilters(page = '1') {
		const params = new URLSearchParams();
		if (query) params.set('q', query);
		if (category !== 'all') params.set('category', category);
		if (author !== 'all') params.set('author', author);
		if (dateRange.start) params.set('from', dateRange.start.toString());
		if (dateRange.end) params.set('to', dateRange.end.toString());
		if (page !== '1') params.set('page', page);
		goto(`?${params}`, { keepFocus: true, noScroll: true, replaceState: true });
	}

	let debounceHandle: ReturnType<typeof setTimeout>;
	function onQueryInput() {
		clearTimeout(debounceHandle);
		debounceHandle = setTimeout(() => applyFilters(), 300);
	}

	function formatDate(iso: string) {
		return new Date(iso).toLocaleDateString(undefined, {
			year: 'numeric',
			month: 'short',
			day: 'numeric'
		});
	}

	const totalPages = $derived(Math.max(Math.ceil(data.total / data.pageSize), 1));
	const loading = $derived(!!navigating.to);
</script>

<div class="mx-auto flex max-w-2xl flex-col gap-4 p-6">
	<div class="flex items-center justify-between">
		<h1 class="text-lg font-semibold">Twitter Datum</h1>
		<ThemeToggle />
	</div>

	<div class="flex flex-col gap-2 rounded-lg border p-3">
		<Input placeholder="Search by content…" bind:value={query} oninput={onQueryInput} />
		<div class="flex flex-wrap gap-2">
			<Select.Root
				type="single"
				bind:value={category}
				onValueChange={() => applyFilters()}
			>
				<Select.Trigger class="w-48">
					{category === 'all' ? 'All categories' : category}
				</Select.Trigger>
				<Select.Content>
					<Select.Item value="all">All categories</Select.Item>
					{#each data.categories as c (c.value)}
						<Select.Item value={c.value!}>{c.value} ({c.count})</Select.Item>
					{/each}
				</Select.Content>
			</Select.Root>
			<Select.Root type="single" bind:value={author} onValueChange={() => applyFilters()}>
				<Select.Trigger class="w-48">
					{author === 'all' ? 'All authors' : `@${author}`}
				</Select.Trigger>
				<Select.Content>
					<Select.Item value="all">All authors</Select.Item>
					{#each data.authors as a (a.username)}
						<Select.Item value={a.username!}>@{a.username} ({a.count})</Select.Item>
					{/each}
				</Select.Content>
			</Select.Root>
			<div class="flex items-center gap-1">
				<Popover.Root>
					<Popover.Trigger class={buttonVariants({ variant: 'outline', class: 'font-normal' })}>
						{rangeLabel}
					</Popover.Trigger>
					<Popover.Content class="w-auto p-0" align="start">
						<RangeCalendar
							bind:value={dateRange}
							onValueChange={() => applyFilters()}
						/>
					</Popover.Content>
				</Popover.Root>
				{#if dateRange.start}
					<Button
						variant="ghost"
						size="icon"
						aria-label="Clear dates"
						onclick={() => {
							dateRange = { start: undefined, end: undefined };
							applyFilters();
						}}
					>
						<X class="size-4" />
					</Button>
				{/if}
			</div>
		</div>
	</div>

	<p class="text-muted-foreground text-sm" class:opacity-50={loading}>
		{data.total} tweets
	</p>

	<div class="flex flex-col gap-3" class:opacity-50={loading}>
		{#each data.tweets as tweet (tweet.id)}
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

	{#if totalPages > 1}
		<div class="flex items-center justify-center gap-3">
			<Button
				variant="outline"
				disabled={data.page <= 1}
				onclick={() => applyFilters(String(data.page - 1))}
			>
				Previous
			</Button>
			<span class="text-muted-foreground text-sm">Page {data.page} of {totalPages}</span>
			<Button
				variant="outline"
				disabled={data.page >= totalPages}
				onclick={() => applyFilters(String(data.page + 1))}
			>
				Next
			</Button>
		</div>
	{/if}
</div>
