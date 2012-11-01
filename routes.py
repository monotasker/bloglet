#!/usr/bin/python
# -*- coding: utf-8 -*-

# default_application, default_controller, default_function
# are used when the respective element is missing from the
# (possibly rewritten) incoming URL

routes_in = (
    ('\b?', '/blog/plugin_blog/index'),
    ('/', '/blog/plugin_blog/index'),
    ('/index', '/blog/plugin_blog/index'),
    ('/index.html', '/blog/plugin_blog/index'),
    ('/login', '/blog/default/user/login'),
    ('/blog/default/index', '/blog/plugin_blog/index'),
    ('/articles/$anything', '/blog/plugin_blog/articles/$anything'),
    ('/classes/$anything', '/blog/plugin_blog/classes/$anything'),
    ('/new_post', '/blog/plugin_blog/new_post'),
    ('/edit_post/$anything', '/blog/plugin_blog/edit_post/$anything'),
    ('/all_posts', '/blog/plugin_blog/all_posts'),
    ('/new_doc', '/blog/plugin_blog/new_doc'),
    # don't break download links
    ('/blog/default/download/$anything', '/blog/default/download/$anything'),
    # make sure you do not break admin
    ('/admin', '/admin'),
    ('/admin/$anything', '/admin/$anything'),
    # make sure you do not break appadmin
    ('/blog/appadmin', '/blog/appadmin'),
    ('/blog/appadmin/$anything', '/blog/appadmin/$anything')
)
routes_out = (
    ('/blog/plugin_blog/index', '/'),
    ('/blog/plugin_blog/articles/$anything', '/articles/$anything'),
    ('/blog/plugin_blog/classes/$anything', '/classes/$anything'),
    ('/blog/plugin_blog/new_post', '/new_post'),
    ('/blog/plugin_blog/edit_post/$anything', '/edit_post/$anything'),
    ('/blog/plugin_blog/all_posts', '/all_posts'),
    ('/blog/plugin_blog/new_doc', '/new_doc'),
    # don't break download links
    ('/blog/default/download/$anything', '/blog/default/download/$anything'),
    # make sure you do not break admin
    ('/admin', '/admin'),
    ('/admin/$anything', '/admin/$anything'),
    # make sure you do not break appadmin
    ('/blog/appadmin', '/blog/appadmin'),
    ('/blog/appadmin/$anything', '/blog/appadmin/$anything')
)
