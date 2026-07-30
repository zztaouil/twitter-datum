<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import * as Avatar from '$lib/components/ui/avatar';
	import { Badge } from '$lib/components/ui/badge';
	import { Button } from '$lib/components/ui/button';
	import Pin from '@lucide/svelte/icons/pin';
	import PinOff from '@lucide/svelte/icons/pin-off';
	import type { Tweet } from '$lib/types';

	let { tweet, onTogglePin }: { tweet: Tweet; onTogglePin: (tweet: Tweet) => void } = $props();

	function formatDate(iso: string) {
		return new Date(iso).toLocaleDateString('fr-FR', {
			year: 'numeric',
			month: 'short',
			day: 'numeric'
		});
	}
</script>

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
				<div class="flex items-center gap-1">
					<Badge variant="secondary">{tweet.category}</Badge>
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
				<span class="text-muted-foreground text-xs">{formatDate(tweet.created_at)}</span>
			</div>
		</div>
	</Card.Header>
	<Card.Content>
		<p class="whitespace-pre-wrap">{tweet.text}</p>
	</Card.Content>
</Card.Root>
