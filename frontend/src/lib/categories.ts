export const CATEGORY_STYLES: Record<string, { bar: string; badge: string; dot: string }> = {
	'digital-influential': {
		bar: 'bg-[#5B7FDE]',
		badge: 'bg-[#EEF1FC] text-[#5B7FDE] dark:bg-[#5B7FDE]/15 dark:text-[#8CA6E8]',
		dot: 'bg-[#5B7FDE]'
	},
	'diplomatic-relational': {
		bar: 'bg-[#D89A3E]',
		badge: 'bg-[#FBF3E4] text-[#B9822F] dark:bg-[#D89A3E]/15 dark:text-[#E3B96B]',
		dot: 'bg-[#D89A3E]'
	},
	'religious-referential': {
		bar: 'bg-[#D97066]',
		badge: 'bg-[#FBEBE9] text-[#C2564C] dark:bg-[#D97066]/15 dark:text-[#E69790]',
		dot: 'bg-[#D97066]'
	},
	unclassified: {
		bar: 'bg-[#7FB8A6]',
		badge: 'bg-[#EBF6F2] text-[#3E8975] dark:bg-[#7FB8A6]/15 dark:text-[#8FCBBB]',
		dot: 'bg-[#7FB8A6]'
	}
};

const FALLBACK = { bar: 'bg-muted-foreground', badge: 'bg-muted text-muted-foreground', dot: 'bg-muted-foreground' };

export function categoryStyle(category: string) {
	return CATEGORY_STYLES[category] ?? FALLBACK;
}

const CATEGORY_LABELS_FR: Record<string, string> = {
	'digital-influential': 'numérique influence',
	'diplomatic-relational': 'diplomatique relationnel',
	'religious-referential': 'référentiel religieux',
	unclassified: 'non classé'
};

export function categoryLabel(category: string) {
	return CATEGORY_LABELS_FR[category] ?? category;
}

export function comboLabel(combo: string) {
	if (combo === 'unclassified') return categoryLabel(combo);
	return combo
		.split(',')
		.map((c) => categoryLabel(c.trim()))
		.join(' + ');
}

// fixed color per category combo, independent of any target's data — keeps a combo's
// color stable across bars (see tools/monitor.ipynb's COMBO_COLORS). "unclassified" is
// omitted on purpose: it carries no insight and would just eat space in every bar.
export const COMBO_COLORS: Record<string, string> = {
	'digital-influential': '#2a78d6',
	'diplomatic-relational': '#eb6834',
	'religious-referential': '#1baf7a',
	'digital-influential,diplomatic-relational': '#eda100',
	'diplomatic-relational,religious-referential': '#e87ba4',
	'digital-influential,religious-referential': '#008300',
	'digital-influential,diplomatic-relational,religious-referential': '#4a3aa7'
};

const compactFormatter = new Intl.NumberFormat('fr-FR', { notation: 'compact', maximumFractionDigits: 1 });

export function formatCompact(n: number) {
	return compactFormatter.format(n);
}
