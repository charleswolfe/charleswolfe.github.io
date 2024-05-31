AUTHOR = 'Charles Wolfe'
SITENAME = 'Chuck Wolfe'
SITEURL = "https://cwolfe.dev/blog/"

PATH = "content"
OUTPUT_PATH = 'blog/'
TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'themes/astro'

# Blogroll
LINKS = (
#    ("Python.org", "https://www.python.org/"),
#    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/charles-wolfe-8b86b331/"),
    ("GitHub", "https://github.com/charleswolfe"),
)

DEFAULT_PAGINATION = 10
DELETE_OUTPUT_DIRECTORY = True
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True