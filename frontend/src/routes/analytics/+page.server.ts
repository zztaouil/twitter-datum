import { PUBLIC_API_URL } from '$env/static/public';
import type { CoverageStat, MediaBackfillStat, ReplyDepthStat, TargetAnalytics } from '$lib/types';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch }) => {
	const [analytics, coverage, media, replyDepth] = await Promise.all([
		fetch(`${PUBLIC_API_URL}/api/analytics`).then((r) => r.json()),
		fetch(`${PUBLIC_API_URL}/api/analytics/coverage`).then((r) => r.json()),
		fetch(`${PUBLIC_API_URL}/api/analytics/media-backfill`).then((r) => r.json()),
		fetch(`${PUBLIC_API_URL}/api/analytics/reply-depth`).then((r) => r.json())
	]);

	return {
		targets: analytics.targets as TargetAnalytics[],
		categories: analytics.categories as string[],
		coverage: coverage.results as CoverageStat[],
		media: media.results as MediaBackfillStat[],
		replyDepth: replyDepth.results as ReplyDepthStat[]
	};
};
