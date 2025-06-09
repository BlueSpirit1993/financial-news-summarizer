from newspaper import Article

def fetch_article_text(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text
