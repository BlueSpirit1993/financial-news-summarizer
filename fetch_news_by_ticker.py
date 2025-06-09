import feedparser

def get_news_for_ticker(ticker):
    feed_url = f"https://news.google.com/rss/search?q={ticker}+stock"
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries[:5]:  # Top 3 articles
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'summary': entry.summary
        })
    return articles
