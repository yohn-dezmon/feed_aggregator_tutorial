import feedparser
import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

f = feedparser.parse('https://www.nasa.gov/rss/dyn/breaking_news.rss')

# print(f) # prints the RSS from the URL

print(dir(f)) # shows you what is in the rss

f.keys()
# this returns the entries available!

#we're going to look at the feed entry !
# this gives us info about the feed itself, but not the articles
# contained within the feed!
f['feed']

# grab the title of our feed
f['feed']['title']

# the actual articles in the feed
# they are stored in a list so you can access them by index!
f['entries']

# pull out first entry
f['entries'][0]

# grab the keys!
f['entries'][0].keys()

# get the title of the first article
f['entries'][0]['title']

# get the link
f['entries'][0]['link']

# published date
f['entries'][0]['published']

# each one has an ID property
# this should be unique for each article
f['entries'][0]['id']

# at some set interval.. 
