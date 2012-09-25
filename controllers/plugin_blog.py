# coding: utf8
if 0:
    from gluon import current
    from gluon.tools import DAL, Crud
    db = DAL()
    crud = Crud()
    request, session, db = current.request, current.session, current.db
    auth = current.auth


def smart_truncate(content, length=300, suffix='...'):
    return (content if len(content) <= length
                    else content[: length].rsplit(' ', 1)[0] + suffix)


def index():
    arts = db(db.articles.id > 0).select(orderby=db.articles.created)
    arts.exclude(lambda row: 5 in row.blog_tags)
    for a in arts:
        if a.teaser == '':
            a.teaser = smart_truncate(a.body)
	a.author = '{} {}'.format(db.auth_user[a.author].first_name,
                                  db.auth_user[a.author].last_name)
    return dict(articles=arts)


def articles():
    the_id = request.args[0]
    arts = db(db.articles.id == the_id).select()
    a = arts.first()
    tags = a.blog_tags
    docs = a.docs
    created = a.created.strftime('%B %e, %Y') or None
    return dict(a=a, created=created, tags=tags, docs=docs)


def classes():
    the_id = request.args[0]
    c = db((db.articles.id == the_id) &
                 (db.articles.blog_tags.contains(5))).select().first()
    tags = c.blog_tags
    alldocs = db(db.docs.id > 0).select()
    docs = alldocs.find(lambda row: row.id in c.docs)
    created = c.created.strftime('%B %e, %Y') or None
    children = db(db.articles.parent == request.args[0]).select()
    parent = db.articles[c.parent]
    return dict(c=c, created=created, tags=tags, docs=docs,
                children=children, parent=parent)


@auth.requires(auth.user_id == 2)
def new_post():
    form = crud.create(db.articles)
    return dict(form=form)


@auth.requires(auth.user_id == 2)
def edit_post():
    form = crud.update(db.articles, request.args[0])
    return dict(form=form)


@auth.requires(auth.user_id == 2)
def new_tag():
    form = crud.create(db.blog_tags)
    return dict(form=form)
