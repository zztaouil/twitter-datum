export interface Tweet {
	id: string;
	text: string;
	created_at: string;
	like_count: number;
	retweet_count: number;
	reply_count: number;
	view_count: number;
	username: string;
	fullname: string;
	category: string;
	pinned?: boolean;
}

export interface Facet {
	username?: string;
	fullname?: string;
	value?: string;
	count: number;
}

export interface TargetAnalytics {
	username: string;
	categories: Facet[];
	total: number;
}
