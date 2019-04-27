from app import app
from db import db
from models import articles, source
import routes
import feed
from threading import Thread
import time
from datetime import datetime

# with creates a context block so anything here
# This tells flask that we're working within our app context...
# when a request is called it creates a context
# it sets up things in the background and we want that setup!
with app.app_context():
    # tell the db to create all the tables we defined.
    db.create_all()
# tell flask to run the application

def update_loop():
    while True:
        with app.app_context():
            query = source.Source.query
            for src in query.all():
                try:
                    update_source(src)
                except:
                    continue
        time.sleep(60) # this waits for 15 minutes...

def update_source(src):
    parsed = feed.parse(src.feed)
    feed_articles = feed.get_articles(parsed)
    articles.Article.insert_from_feed(src.id, feed_articles)
    print("Updated" + src.feed)

def delete_old_articles():
    while True:
        with app.app_context():
            try:
                articles.Article.delete_from_db()
                print("success")
            except:
                continue
        time.sleep(60)


update_loop()
delete_old_articles()


app.run()
