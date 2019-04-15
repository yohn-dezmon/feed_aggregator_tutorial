from app import app
from models import articles
import feed
from models import source

def inserting_sources(feedz):
    """ inserting sources """
    parsed = feed.parse(feedz)
    feed_source = feed.get_source(parsed)
    return feed_source

cumulative_list = []

def inserting_articles(feedz):
    parsed = feed.parse(feedz)
    feed_articles = feed.get_articles(parsed)
    return feed_articles


nasa_url = 'https://www.nasa.gov/rss/dyn/breaking_news.rss'
reuters_env_url = 'http://feeds.reuters.com/reuters/environment'

list_of_urls = [nasa_url, wired_url]



# get into flask app context
with app.app_context():

    for url in list_of_urls:
        inserting_articles(url)

    articles.Article.insert_from_feed(source.id, cumulative_list)
