#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daphnée PORTHEAULT'
SITENAME = 'A Biologist Lost in Data'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['image']
THEME = 'theme/blueidea'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
DISPLAY_AUTHOR_ON_POSTINFO = True
DISPLAY_CATEGORIES_ON_SUBMENU = True
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Theme by Nasskach', 'https://github.com/nasskach/pelican-blueidea'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/Elesh-Norn'),
          ('Linkedin', 'https://www.linkedin.com/in/daphn%C3%A9e-portheault-96b2b810a/'),
          ('Email', 'mailto:daphnee.portheault@protonmail.com'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
