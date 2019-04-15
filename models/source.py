from db import db
import datetime

# This tells SQLAlchemy that everything you define within this class is part of a
# db model!
class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    subtitle = db.Column(db.Text, nullable=False)
    # the link here is a link to nasa's website
    link = db.Column(db.Text, nullable=False)
    # link to RSS feed
    feed = db.Column(db.Text, nullable=False)
    # when we create a 'source' we don't have to tell it when it was added
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    """ You would never call a class method on an instance of Source, rather
    you call it on Source itself. 'cls' here is like self within a class.
    The feed URL (feed) must be included as an arg since it cannot be null
    feed_source = parsed feed"""
    @classmethod
    def insert_from_feed(cls, feed, feed_source):
        """ the feed_source will be the feed variable from the get_source method of feed.py"""
        link = feed_source['link']
        title = feed_source['title']
        subtitle = feed_source['subtitle']
        source = Source(feed=feed, link=link, title=title, subtitle=subtitle)
        db.session.add(source)
        db.session.commit()
        return source
