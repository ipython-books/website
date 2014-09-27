


# make sure to end all internal links with '/' so that mod_rewrite .htaccess works 
# with subdirectories
# SITEURL = 'http://cyrille.rossant.net'
SITEURL = ''  # FOR LOCAL DEV ONLY

AUTHOR = 'Cyrille Rossant'
SITENAME = "IPython Books"
DISQUS_SITENAME = 'ipython-books'
LOCALE = 'en_US.utf8'
PATH = 'content'
THEME = 'themes/pure'
STATIC_PATHS = ['images']
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU  = False
DEFAULT_DATE = 'fs'
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

MD_EXTENSIONS = ['codehilite(css_class=highlight,guess_lang=False,linenums=False)',
				 'extra']

DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [
			'pelican_plugin-render_math',
			'summary', 
			'neighbors',
]

# OUTPUT_PATH = '../rossant.github.io'

DEFAULT_CATEGORY = ''

DIRECT_TEMPLATES = ('index', 'archives')

ARCHIVES_SAVE_AS = ''

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TAG_URL = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''

AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''




TWITTER_USERNAME = 'cyrillerossant'
MENUITEMS = [('Home', '/'),
             ('Minibook', '/minibook/'),
             ('Cookbook', '/cookbook/'),
             ('Author', 'http://cyrille.rossant.net'),
            ]
DATE_FORMATS = {
    'en': '%Y-%m-%d',
}


PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
# FEED_ATOM = 'feeds/atom.xml'
# FEED_RSS = 'feeds/rss.xml'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

FEED_DOMAIN = SITEURL
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

