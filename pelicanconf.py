#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yusei Nishiyama'
SITENAME = u'\u3060\u304b\u3089\u3068\u3044\u3063\u3066\u3001\u3053\u306e\u307e\u307e\u3067\u3044\u3044\u306f\u305a\u304c\u306a\u3044\u3002'
SITEURL = 'http://yuseinishiyama.com'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/yuseinishiyama'),
          ('github', 'https://github.com/yuseinishiyama'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/Users/nishiyama_y/Workspace/pelican/using-theme/sundown-copy"

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/.htaccess', 'extra/robots.txt']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/.htaccess': {'path': '.htaccess'},}
# 記事のURL
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'

# 記事の保存先
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# カテゴリのURL
CATEGORY_URL = "category/{slug}"

# カテゴリの保存先
CATEGORY_SAVE_AS = "category/{slug}/index.html"

# タグのURL
TAG_URL = "tag/{slug}/"

# タグの保存先
TAG_SAVE_AS = "tag/{slug}/index.html"

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Google Analytics
GOOGLE_ANALYTICS = 'UA-48020408-1'

# Disqus
DISQUS_SITENAME = 'yuseinishiyama'
