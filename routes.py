#!/usr/bin/python
# -*- coding: utf-8 -*-

# default_application, default_controller, default_function
# are used when the respective element is missing from the
# (possibly rewritten) incoming URL

routes_in = (
    ('/index', '/blog/plugin_blog/index'),
    ('/articles/$anything', '/blog/plugin_blog/articles/$anything'),
    ('/classes/$anything', '/blog/plugin_blog/classes/$anything'),
    ('/blog/default/download/$anything', '/blog/default/download/$anything'),
    # make sure you do not break admin
    ('/admin', '/admin'),
    ('/admin/$anything', '/admin/$anything'),
    # make sure you do not break appadmin
    ('/blog/appadmin', '/blog/appadmin'),
    ('/blog/appadmin/$anything', '/blog/appadmin/$anything'),
)
routes_out = [(x, y) for (y, x) in routes_in]
