import { PUBLIC_API_URL } from '$env/static/public';
import type { Facet } from '$lib/types';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ fetch }) => {
	try {
		const res = await fetch(`${PUBLIC_API_URL}/api/facets`);
		if (!res.ok) throw new Error(`facets ${res.status}`);
		const facets = await res.json();
		return {
			categories: facets.categories as Facet[],
			authors: facets.authors as Facet[]
		};
	} catch {
		// ponytail: API unreachable (dev backend not up), degrade instead of 500ing every page
		return { categories: [] as Facet[], authors: [] as Facet[] };
	}
};
