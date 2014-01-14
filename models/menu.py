# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

if 0:
    from gluon import T, URL, current, SPAN
    response = current.response
    request = current.request

response.title = T('Confessions of a Monotasker')
response.mobiletitle = response.title
response.subtitle = T('Ian W. Scott')
response.right_sidebar_enabled = 4
response.left_sidebar_enabled = 0

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Ian W. Scott <scottianw@gmail.com>'
response.meta.description = 'My blog for biblical studies, web development,'\
                            ' and life in general.'
response.meta.keywords = 'bible, biblical, studies, academic, scholarship,'\
                        ' web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'
response.meta.copyright = 'All content copyright Ian W. Scott, 2012—2014 unless'\
                        ' otherwise specified (all rights reserved); Site'\
                        ' design copyright Ian W. Scott (licensed under'\
                        ' GPL 3.0).'

## your http://google.com/analytics id
response.google_analytics_id = None

## default sidebar blocks
rightblocks = ['info', 'hours', 'my_sites', 'student_aids', 'classes']
# 'social'

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [(SPAN(T(' Home'), _class='icon-home'), False,
                  URL('default', 'index'), []),
                 (SPAN(T(' Browse Topics'), _class='icon-tag'), False,
                  URL('plugin_blog', 'topic', args=[]), []),
                 ]


if auth.has_membership('administrators'):
    response.menu.extend([(SPAN(T(' Edit'), _class='icon-cog'), False,
                        URL('plugin_blog', 'editing', args=['articles']),
                            [(SPAN(T(' Articles'), _class='icon-home'), False,
                            URL('plugin_blog', 'editing', args=['articles']), []),
                            (SPAN(T(' Tags'), _class='icon-home'), False,
                            URL('plugin_blog', 'editing', args=['blog_tags']), []),
                            (SPAN(T(' Documents'), _class='icon-home'), False,
                            URL('plugin_blog', 'editing', args=['documents']), []),
                            ]),
                        ])
    #def _():
        ## shortcuts
        #app = request.application
        #ctr = request.controller
