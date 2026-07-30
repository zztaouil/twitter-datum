<script lang="ts">
	import { goto } from '$app/navigation';
	import { navigating } from '$app/state';
	import { PUBLIC_API_URL } from '$env/static/public';
	import { Input } from '$lib/components/ui/input';
	import * as Select from '$lib/components/ui/select';
	import * as Popover from '$lib/components/ui/popover';
	import { RangeCalendar } from '$lib/components/ui/range-calendar';
	import { Button, buttonVariants } from '$lib/components/ui/button';
	import { DateFormatter, getLocalTimeZone, parseDate } from '@internationalized/date';
	import type { DateRange } from 'bits-ui';
	import X from '@lucide/svelte/icons/x';
	import TweetCard from '$lib/components/tweet-card.svelte';
	import type { Tweet } from '$lib/types';
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();

	let tweets = $state(data.tweets);
	$effect(() => {
		tweets = data.tweets;
	});

	async function togglePin(tweet: Tweet) {
		const pinned = !tweet.pinned;
		tweets = tweets.map((t) => (t.id === tweet.id ? { ...t, pinned } : t));
		if (pinned) {
			await fetch(`${PUBLIC_API_URL}/api/pins`, {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ tweet_id: tweet.id })
			});
		} else {
			await fetch(`${PUBLIC_API_URL}/api/pins/${tweet.id}`, { method: 'DELETE' });
		}
	}

	const df = new DateFormatter('fr-FR', { dateStyle: 'medium' });

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
		if (!dateRange.start) return 'Toutes les dates';
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

	const totalPages = $derived(Math.max(Math.ceil(data.total / data.pageSize), 1));
	const loading = $derived(!!navigating.to);
</script>

<h1 class="text-xl font-bold">Recherche</h1>

<div class="flex flex-col gap-2 rounded-lg border p-3">
	<Input placeholder="Rechercher par contenu…" bind:value={query} oninput={onQueryInput} />
	<div class="flex flex-wrap gap-2">
		<Select.Root type="single" bind:value={author} onValueChange={() => applyFilters()}>
			<Select.Trigger class="w-48">
				{author === 'all' ? 'Tous les auteurs' : `@${author}`}
			</Select.Trigger>
			<Select.Content>
				<Select.Item value="all">Tous les auteurs</Select.Item>
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
					<RangeCalendar bind:value={dateRange} onValueChange={() => applyFilters()} />
				</Popover.Content>
			</Popover.Root>
			{#if dateRange.start}
				<Button
					variant="ghost"
					size="icon"
					aria-label="Effacer les dates"
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

<div class="grid grid-cols-1 gap-4 lg:grid-cols-2" class:opacity-50={loading}>
	{#each tweets as tweet (tweet.id)}
		<TweetCard {tweet} onTogglePin={togglePin} />
	{:else}
		<p class="text-muted-foreground py-8 text-center lg:col-span-2">
			Aucun tweet ne correspond à vos filtres.
		</p>
	{/each}
</div>

{#if totalPages > 1}
	<div class="flex items-center justify-center gap-3">
		<Button
			variant="outline"
			disabled={data.page <= 1}
			onclick={() => applyFilters(String(data.page - 1))}
		>
			Précédent
		</Button>
		<span class="text-muted-foreground text-sm">Page {data.page} sur {totalPages}</span>
		<Button
			variant="outline"
			disabled={data.page >= totalPages}
			onclick={() => applyFilters(String(data.page + 1))}
		>
			Suivant
		</Button>
	</div>
{/if}
