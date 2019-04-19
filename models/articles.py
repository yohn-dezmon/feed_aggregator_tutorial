from db import db
import datetime

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    # link to the article
    link = db.Column(db.Text, nullable=False)
    guid = db.Column(db.String(255), nullable=False)
    unread = db.Column(db.Boolean, default=True, nullable=False)
    # the objects have a relationship to the source!
    # where does this come from? source.py?
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'), nullable=False)
    # this tells sqlAlchemy that the Source class is the table we want the id from
    # backreference is the article... so it gives source an attribute which is a list of the articles?
    # lazy means that it won't pull the articles every time the source is pulled...

    source = db.relationship('Source', backref=db.backref('articles', lazy=True))
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    # this is from feed.py... articles [published].
    date_published = db.Column(db.DateTime)
    # this is a constraint. a unique constraint.
    # we don't want any two articles to have the same source id
    # you insert the columns that are going to be unique!
    # you must follow the object with a comma to indicate that this is a one element tuple
    __table_args__ = (
        db.UniqueConstraint('source_id','guid', name='uc_source_guid'),
    )

    """ cls here is like self within a class """
    @classmethod
    def insert_from_feed(cls, source_id, feed_articles):
        """ feed_articles is from get_articles of the feed.py module"""
        # stmt accounts for when SQLAlchemy attempts to reinsert an article from the list
        # with the same guid and source id [see uniqueconstraint]
        stmt = Article.__table__.insert().prefix_with('IGNORE')
        articles = []
        # why are we appending a dictionary to a list?
        for article in feed_articles:
            articles.append({
                'title': article['title'],
                'body': article['summary'],
                'link': article['link'],
                'guid': article['id'],
                'source_id': source_id,
                'date_published': article['published'],
            })
            # the execute line will do a batch insert of all of hte articles in the list! :D
        db.engine.execute(stmt, articles)

    @classmethod
    def delete_from_db(cls):
        """ Delete articles that have been in the db for >= x days"""
        now = datetime.datetime.utcnow()
        now_day = now.day
        delt_time_diff = datetime.timedelta(3)
        time_diff = delt_time_diff.days

        query = Article.query
        for article in query.all():
            date_added = article.date_added
            date_added_day = date_added.day
            # note to self: here now isn't a specific value, in the argument place or in the retun statement!
            def subtract_date(now, date_added):
                return now - date_added




                # here now is referring to the variable defined previously! :D
            d = Article.__table__.delete().where(subtract_date(now_day, date_added_day) >= time_diff)
            db.engine.execute(d)
