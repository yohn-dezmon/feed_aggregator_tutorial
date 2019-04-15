import feedparser

import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

parsed = feedparser.parse('http://planetpython.org/rss20.xml')
