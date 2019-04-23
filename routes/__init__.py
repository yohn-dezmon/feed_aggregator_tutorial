from flask import abort, redirect, request, render_template
from app import app
from models.articles import Article
from models.source import Source
from db import db
import feed
# the index page!
# this will display all articles... (unread)
@app.route('/', methods=['GET'])
def index_get():
    # since Article is defined as  Article(db.Model): it has a .query attribute
    query = Article.query
    def query_over(query, src_id):
        query = query.filter(Article.unread == True, Article.source_id == src_id)
        query = query.order_by(Article.date_added.desc())
        return query.all()

# this should be automated better, to query for available source ids, and for all source ids it should create an articles box...
    first_articles = query_over(query, 1)
    second_articles = query_over(query, 2)
    third_articles = query_over(query, 3)
    fourth_articles = query_over(query, 5)

    # when you redeine the query_1 variableon each line, you are constructing a SQL select statement


    return render_template('index.html', first_articles=first_articles,
                            second_articles=second_articles,
                            third_articles=third_articles,
                            fourth_articles=fourth_articles)

# <article_id> is a path variable!
# what ever you name that variable in the path, will be passed to the variable name in the function
# can you assign the article_id from a different hanlder? probably...
@app.route('/read/<int:article_id>', methods=['GET'])
def read_article_get(article_id):
    # hmmm is article here an instantiation of Article table?
    article = Article.query.get(article_id)
    article.unread = False
    db.session.commit()
    # redirecting to the article linK! :D
    return redirect(article.link)

@app.route('/sources', methods=['GET'])
def sources_get():
    query = Source.query
    query = query.order_by(Source.title)
    sources = query.all()
    return render_template('sources.html', sources=sources)


@app.route('/sources', methods=['POST'])
def sources_post():
    # a form is going to be submitted here that has a 'feed' field
    # where feed is a url
    feed_url = request.form['feed']
    parsed = feed.parse(feed_url)
    feed_source = feed.get_source(parsed)
    # put it into the db
    source = Source.insert_from_feed(feed_url, feed_source)
    return redirect('/sources')
