#!/usr/bin/python
# -*- coding: utf-8 -*-

# default_application, default_controller, default_function
# are used when the respective element is missing from the
# (possibly rewritten) incoming URL
#
default_application = 'bloglet'    # ordinarily set in base routes.py
default_controller = 'plugin_blog'  # ordinarily set in app-specific routes.py

routes_in = (
    ('/articles/$anything', '/bloglet/plugin_blog/articles/$anything'),
    ('/index', '/bloglet/plugin_blog/index'),
    ('/index', '/bloglet/plugin_blog/front'),
)
routes_out = [(x, y) for (y, x) in routes_in]

