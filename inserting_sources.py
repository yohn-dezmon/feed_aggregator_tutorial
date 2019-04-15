from app import app
from models import articles
import feed

nasa_url = 'https://www.nasa.gov/rss/dyn/breaking_news.rss'
reuters_env_url = 'http://feeds.reuters.com/reuters/environment'

list_of_urls = [nasa_url, wired_url]

def inserting_feedz(feedz):
    parsed = feed.parse(feedz)
    feed_source = feed.get_source(parsed)
    return feed_source


# get into flask app context
# 1 = source_id ! :D does this just mean that this is where this starts?
with app.app_context():

    for url in list_of_urls:
        inserting_feedz(url)
        articles.Source.insert_from_feed(url, feed_source)
