#!/usr/bin/python
# -*- coding: utf-8 -*-

# default_application, default_controller, default_function
# are used when the respective element is missing from the
# (possibly rewritten) incoming URL
#
default_controller = 'plugin_blog'  # ordinarily set in app-specific routes.py

routes_in = (
    ('/articles/$anything', '/home/plugin_blog/articles/$anything'),
    ('/index', '/home/plugin_blog/index'),
    ('/classes/$anything', '/home/plugin_blog/classes/$anything')
)
routes_out = [(x, y) for (y, x) in routes_in]
