#! /usr/bin/python
# -*-coding:utf8-*-

import datetime
import os
from plugin_ajaxselect import AjaxSelect

if 0:
    from gluon import current, IS_IN_DB, Field, IS_EMPTY_OR, URL
    db = current.db
    auth = current.auth
    request = current.request
    response = current.response

response.files.insert(5, URL('static',
                      'plugin_ajaxselect/plugin_ajaxselect.js'))

db.define_table('blog_images',
                Field('uid', 'integer'),
                Field('image_title', length=512),
                Field('image_description', 'text'),
                Field('img_file', 'upload', length=256,
                      uploadfolder='static/images'),
                format=lambda r: r.image_title)

db.define_table('blog_tags',
    Field('tagname'),
    format='%(tagname)s')

db.define_table('docs',
    Field('label'),
    Field('docfile', 'upload', length=200, uploadfield=True,
          uploadfolder=os.path.join(request.folder, 'uploads')),
    format='%(label)s')

db.define_table('blog_links',
    Field('link_label'),
    Field('url'),
    Field('description', 'text'),
    format='%(link_label)s')

db.define_table('articles',
    Field('author', db.auth_user, default=auth.user_id),
    Field('title'),
    Field('created', 'datetime', default=datetime.datetime.now()),
    Field('body', 'text'),
    Field('teaser', 'text'),
    Field('pullquote', 'text'),
    Field('blog_tags', 'list:reference blog_tags'),
    Field('parent', 'reference articles'),
    Field('docs', 'list:reference docs'),
    Field('blog_links', 'list:reference blog_links'),
    format='%(title)s')
db.articles.parent.requires = IS_EMPTY_OR(IS_IN_DB(db, 'articles.id',
                                                   db.articles._format,
                                                   multiple=False))
db.articles.blog_tags.requires = IS_IN_DB(db, 'blog_tags.id',
                                          db.blog_tags._format,
                                          multiple=True)
db.articles.blog_tags.widget = lambda field, value: \
                                AjaxSelect(field, value,
                                            indx=1,
                                            refresher=True,
                                            multi='basic',
                                            lister='simple',
                                            orderby='tagname').widget()
db.articles.docs.requires = IS_EMPTY_OR(IS_IN_DB(db, 'docs.id',
                                                 db.docs._format,
                                                 multiple=True))
db.articles.docs.widget = lambda field, value: \
                          AjaxSelect(field, value,
                                     indx=2,
                                     refresher=True,
                                     multi='basic',
                                     lister='simple',
                                     orderby='label').widget()
