import datetime
import os

if 0:
    from gluon import current, IS_IN_DB, Field
    db = current.db
    auth = current.auth
    request = current.request


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

db.articles.blog_tags.requires = IS_IN_DB(db, 'blog_tags.id',
                                          db.blog_tags._format,
                                          multiple=True)
db.articles.docs.requires = IS_IN_DB(db, 'docs.id',
                                          db.docs._format,
                                          multiple=True)
