# coding: utf8
if 0:
    from gluon import current
    from gluon.tools import DAL, Crud
    db = DAL()
    crud = Crud()
    request, session, db, auth = current.request, current.session, current.db, current.auth

def front():
    arts = db(db.articles.id > 0).select(orderby = db.articles.created)
    return dict(articles = arts)

def articles():
    the_id = request.args[0]
    art = db(db.articles.id == the_id).select()
    a = art[0]
    created = a.created.strftime('%B %e, %Y')
    return dict(a = a, created = created)

@auth.requires(auth.user_id == 1)
def new_post():
    form = crud.create(db.articles)
    return dict(form = form)

@auth.requires(auth.user_id == 1)
def edit_post():
    form = crud.update(db.articles)
    return dict(form = form)

@auth.requires(auth.user_id == 1)
def new_tag():
    form = crud.create(db.blog_tags)
    return dict(form = form)
