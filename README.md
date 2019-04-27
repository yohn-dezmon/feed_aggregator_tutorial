#DavyBot's Feed Reader Tutorial

This is a content aggregator that was made by following DavyBot's tutorial that can be
found here: https://www.youtube.com/watch?v=8rvvFNKHUss&list=PLmxT2pVYo5LBcv5nYKTIn-fblphtD_OJO or https://github.com/code-tutorials/python-feedreader

I watched all videos except 08 and 10.

**The functionality I added myself:**

1. A function that deletes all articles that have been in the DB for more than X days. (articles.py)
2. custom CSS (styles.css of static )
3. CSS/html to display four boxes (styles.css of static/index.html of templates/ __init__.py of routes)
4. a call to insert the articles after the new source has been added in the
/sources route... (__init__.py of routes))
5. using crontab to run run.py every minute. [* * * * * /Users/HomeFolder/.venvs/tentagg/bin/Python /Users/HomeFolder/taskqueue_tut/run.py]
6. Fixed the body/article['summary'] portion of each article such that it doesn't display any html tags!
