import { PUBLIC_API_URL } from '$env/static/public';
import type {
	CategoryComboStat,
	CoverageStat,
	MediaBackfillStat,
	ReplyDepthStat,
	TargetAnalytics
} from '$lib/types';
import type { PageServerLoad } from './$types';

// ponytail: these queries can take a couple seconds on a cold cache — stream each
// section in independently instead of blocking the whole page on the slowest one.
export const load: PageServerLoad = async ({ fetch }) => {
	const getJson = (path: string) => fetch(`${PUBLIC_API_URL}${path}`).then((r) => r.json());

	return {
		analytics: getJson('/api/analytics') as Promise<{
			targets: TargetAnalytics[];
			categories: string[];
		}>,
		combos: getJson('/api/analytics/category-combos') as Promise<{
			results: CategoryComboStat[];
			combos: string[];
		}>,
		coverage: getJson('/api/analytics/coverage') as Promise<{ results: CoverageStat[] }>,
		media: getJson('/api/analytics/media-backfill') as Promise<{ results: MediaBackfillStat[] }>,
		replyDepth: getJson('/api/analytics/reply-depth') as Promise<{ results: ReplyDepthStat[] }>
	};
};
