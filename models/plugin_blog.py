db.define_table('blog_tags',
    Field('tagname'),
    format='%(tagname)s')

db.define_table('articles',
    Field('author', db.auth_user, default = auth.user_id),
    Field('title'),
    Field('created', 'datetime'),
    Field('body', 'text'),
    Field('teaser', 'text'),
    Field('pullquote', 'text'),
    Field('blog_tags', db.blog_tags),
    format='%(title)s')
