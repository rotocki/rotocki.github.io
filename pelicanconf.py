#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Remik'
SITENAME = 'Accruing technical credit'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'EN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('rotocki', 'https://github.com/rotocki/'),
#          ('rotocki', 'https://www.linkedin.com/in/remigiuszotocki/'),)

DEFAULT_PAGINATION = 10

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

MENUITEMS = (
    ('Home', '/'),
    # ('Archives', '/archives.html'),
    # ('About me', '/pages/about-me.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True