<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import * as Avatar from '$lib/components/ui/avatar';
	import { Badge } from '$lib/components/ui/badge';
	import { Button } from '$lib/components/ui/button';
	import Pin from '@lucide/svelte/icons/pin';
	import PinOff from '@lucide/svelte/icons/pin-off';
	import { categoryStyle, categoryLabel } from '$lib/categories';
	import type { Tweet } from '$lib/types';

	let { tweet, onTogglePin }: { tweet: Tweet; onTogglePin: (tweet: Tweet) => void } = $props();

	// categories are ranked strongest-match first — use it for the accent bar
	const style = $derived(categoryStyle(tweet.categories[0]));

	function formatDate(iso: string) {
		return new Date(iso).toLocaleDateString('fr-FR', {
			year: 'numeric',
			month: 'short',
			day: 'numeric'
		});
	}
</script>

<Card.Root class="relative">
	<div class="absolute inset-y-0 left-0 w-1.5 {style.bar}"></div>
	<Card.Header>
		<div class="flex items-center gap-3">
			<Avatar.Root>
				<Avatar.Fallback>{tweet.username[0]?.toUpperCase()}</Avatar.Fallback>
			</Avatar.Root>
			<div class="flex flex-1 flex-col">
				<span class="font-arabic font-bold">{tweet.fullname}</span>
				<span class="text-muted-foreground text-sm">@{tweet.username}</span>
			</div>
			<div class="flex flex-col items-end gap-1">
				<div class="flex flex-wrap items-center justify-end gap-1">
					{#each tweet.categories as category (category)}
						<Badge class={categoryStyle(category).badge}>{categoryLabel(category)}</Badge>
					{/each}
					<Button
						variant="ghost"
						size="icon-sm"
						class={tweet.pinned ? 'text-primary hover:text-primary' : ''}
						aria-label={tweet.pinned ? 'Désépingler le tweet' : 'Épingler le tweet'}
						onclick={() => onTogglePin(tweet)}
					>
						{#if tweet.pinned}
							<PinOff class="size-4" />
						{:else}
							<Pin class="size-4" />
						{/if}
					</Button>
				</div>
				<span class="text-muted-foreground font-mono text-xs">{formatDate(tweet.created_at)}</span>
			</div>
		</div>
	</Card.Header>
	<Card.Content>
		<p class="font-arabic whitespace-pre-wrap leading-relaxed" dir="auto">{tweet.text}</p>
	</Card.Content>
</Card.Root>
