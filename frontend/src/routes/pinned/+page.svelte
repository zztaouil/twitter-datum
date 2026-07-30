<script lang="ts">
	import { PUBLIC_API_URL } from '$env/static/public';
	import { Button } from '$lib/components/ui/button';
	import TweetCard from '$lib/components/tweet-card.svelte';
	import type { Tweet } from '$lib/types';
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();
	let tweets = $state(data.tweets);

	$effect(() => {
		tweets = data.tweets;
	});

	async function unpin(tweet: Tweet) {
		tweets = tweets.filter((t) => t.id !== tweet.id);
		await fetch(`${PUBLIC_API_URL}/api/pins/${tweet.id}`, { method: 'DELETE' });
	}

	async function unpinAll() {
		tweets = [];
		await fetch(`${PUBLIC_API_URL}/api/pins`, { method: 'DELETE' });
	}
</script>

<div class="flex items-center justify-between">
	<p class="text-muted-foreground text-sm">{tweets.length} pinned tweets</p>
	{#if tweets.length}
		<Button variant="outline" size="sm" onclick={unpinAll}>Unpin all</Button>
	{/if}
</div>

<div class="flex flex-col gap-3">
	{#each tweets as tweet (tweet.id)}
		<TweetCard {tweet} onTogglePin={unpin} />
	{:else}
		<p class="text-muted-foreground py-8 text-center">No pinned tweets yet.</p>
	{/each}
</div>
