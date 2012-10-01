# coding: utf8
if 0:
    from gluon import current
    from gluon.tools import DAL, Crud
    db = DAL()
    crud = Crud()
    request, session, db = current.request, current.session, current.db
    auth = current.auth


def index():
    arts = db(db.articles.id > 0).select(orderby=db.articles.created)
    return dict(articles=arts)


def articles():
    the_id = request.args[0]
    art = db(db.articles.id == the_id).select()
    a = art[0]
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
