import { PUBLIC_API_URL } from '$env/static/public';
import type { Tweet } from '$lib/types';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ url, fetch }) => {
	const q = url.searchParams.get('q') ?? '';
	const category = url.searchParams.get('category') ?? '';
	const authors = url.searchParams.getAll('author');
	const from = url.searchParams.get('from') ?? '';
	const to = url.searchParams.get('to') ?? '';
	const page = url.searchParams.get('page') ?? '1';

	const searchParams = new URLSearchParams({ page, page_size: '20' });
	if (q) searchParams.set('q', q);
	if (category) searchParams.set('category', category);
	for (const author of authors) searchParams.append('author', author);
	if (from) searchParams.set('from', from);
	if (to) searchParams.set('to', to);

	const search = await (await fetch(`${PUBLIC_API_URL}/api/search?${searchParams}`)).json();

	return {
		tweets: search.results as Tweet[],
		total: search.total as number,
		page: search.page as number,
		pageSize: search.page_size as number,
		filters: { q, category, authors, from, to }
	};
};
