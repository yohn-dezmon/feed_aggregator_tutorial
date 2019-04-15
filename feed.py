import feedparser

import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context


def parse(url):
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
    return feedparser.parse(url)

def get_source(parsed):
    """ the origin of the data """

    feed = parsed['feed']
    # this link is a specific URL for the article/entry
    # these will be columns in our db
    return {
        'link': feed['link'],
        'title': feed['title'],
        'subtitle': feed['subtitle'],
    }

def get_articles(parsed):
    """ Return a list of articles in this parsed feed """
    entries = parsed['entries']
    articles = []
    # for each entry we're going to append a dictionary!
    for entry in entries:
        articles.append({
            'id': entry['id'],
            'link': entry['link'],
            'title': entry['title'],
            'summary': entry['summary'],
            'published': entry['published_parsed'],

        })
    return articles
