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

export interface CoverageStat {
	username: string;
	tweets_count: number;
	own: number;
	total: number;
	pct: number;
}

export interface MediaBackfillStat {
	username: string;
	done: number;
	total: number;
	pct: number;
}

export interface ReplyDepthStat {
	username: string;
	tweets: number;
	l1_replies: number;
	l2_replies: number;
	l1_per_tweet: number;
	l2_per_tweet: number;
}
