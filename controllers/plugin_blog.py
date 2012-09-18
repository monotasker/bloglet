# coding: utf8
if 0:
    from gluon import current
    from gluon.tools import DAL, Crud
    db = DAL()
    crud = Crud()
    request, session, db, auth = current.request, current.session, current.db, current.auth

def index():
    arts = db(db.articles.id > 0).select(orderby = db.articles.created)
    return dict(articles = arts)

def articles():
    the_id = request.args[0]
    art = db(db.articles.id == the_id).select()
    a = art[0]
    tags = a.tags
    created = a.created.strftime('%B %e, %Y') or None
    return dict(a = a, created = created, tags=tags)

@auth.requires(auth.user_id == 2)
def new_post():
    form = crud.create(db.articles)
    return dict(form = form)

@auth.requires(auth.user_id == 2)
def edit_post():
    form = crud.update(db.articles)
    return dict(form = form)

@auth.requires(auth.user_id == 2)
def new_tag():
    form = crud.create(db.blog_tags)
    return dict(form = form)
