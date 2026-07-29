import { PUBLIC_API_URL } from '$env/static/public';
import type { Facet } from '$lib/types';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ fetch }) => {
	const res = await fetch(`${PUBLIC_API_URL}/api/facets`);
	const facets = await res.json();
	return {
		categories: facets.categories as Facet[],
		authors: facets.authors as Facet[]
	};
};
