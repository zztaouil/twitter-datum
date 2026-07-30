<script lang="ts">
	import { goto } from '$app/navigation';
	import { navigating, page } from '$app/state';
	import { PUBLIC_API_URL } from '$env/static/public';
	import { Input } from '$lib/components/ui/input';
	import { Button } from '$lib/components/ui/button';
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

	let query = $state(data.filters.q);

	// keep controls in sync with back/forward navigation, which changes `data` without going through applyFilters
	$effect(() => {
		query = data.filters.q;
	});

	// preserves category/author/date filters already in the URL, managed by the sidebar
	function applyFilters(pageNum = '1') {
		const params = new URLSearchParams(page.url.searchParams);
		if (query) params.set('q', query);
		else params.delete('q');
		if (pageNum !== '1') params.set('page', pageNum);
		else params.delete('page');
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

<div class="rounded-lg border p-3">
	<Input placeholder="Rechercher par contenu…" bind:value={query} oninput={onQueryInput} />
</div>

<p class="text-sm text-muted-foreground" class:opacity-50={loading}>
	{data.total} tweets
</p>

<div class="grid grid-cols-1 gap-4 lg:grid-cols-2" class:opacity-50={loading}>
	{#each tweets as tweet (tweet.id)}
		<TweetCard {tweet} onTogglePin={togglePin} />
	{:else}
		<p class="py-8 text-center text-muted-foreground lg:col-span-2">
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
		<span class="text-sm text-muted-foreground">Page {data.page} sur {totalPages}</span>
		<Button
			variant="outline"
			disabled={data.page >= totalPages}
			onclick={() => applyFilters(String(data.page + 1))}
		>
			Suivant
		</Button>
	</div>
{/if}
