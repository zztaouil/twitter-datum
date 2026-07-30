import { PUBLIC_API_URL } from '$env/static/public';
import type { TargetAnalytics } from '$lib/types';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch }) => {
	const res = await (await fetch(`${PUBLIC_API_URL}/api/analytics`)).json();
	return {
		targets: res.targets as TargetAnalytics[],
		categories: res.categories as string[]
	};
};
