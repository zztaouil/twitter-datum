import { PUBLIC_API_URL } from '$env/static/public';
import type { Tweet } from '$lib/types';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch }) => {
	const res = await (await fetch(`${PUBLIC_API_URL}/api/pins`)).json();
	return {
		tweets: (res.results as Tweet[]).map((t) => ({ ...t, pinned: true }))
	};
};
