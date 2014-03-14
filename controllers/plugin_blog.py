# -*- coding: utf-8 -*-

if 0:
    from gluon import current
    from gluon.tools import DAL, Crud
    db = DAL()
    crud = Crud()
    request, session, db = current.request, current.session, current.db
    auth = current.auth

import re
from pprint import pprint


def smart_truncate(content, length=480, suffix='...'):
    return (content if len(content) <= length
            else content[: length].rsplit(' ', 1)[0] + suffix)


def index():
    arts = db(db.articles.id > 0).select(orderby=~db.articles.created)
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
    art = arts.first()
    tags = [db.blog_tags[t].tagname for t in art.blog_tags]
    docs = art.docs
    created = art.created.strftime('%B %e, %Y') or None
    return dict(art=art, created=created, tags=tags, docs=docs)


def classes():
    print 'starting classes controller'
    docrows = db(db.docs.id > 0).select().as_list()
    pprint(docrows)
    the_id = request.args[0]
    myclass = db((db.articles.id == the_id) &
                 (db.articles.blog_tags.contains(5))).select().first()
    tags = myclass.blog_tags
    alldocs = db(db.docs.id > 0).select()
    docs = alldocs.find(lambda row: row.id in myclass.docs)
    created = myclass.created.strftime('%B %e, %Y') or None
    children = db(db.articles.parent == request.args[0]).select()
    parent = db.articles[myclass.parent]
    return dict(myclass=myclass, created=created, tags=tags, docs=docs,
                children=children, parent=parent)


@auth.requires(auth.user_id == 2)
def editing():
    parent = None
    children = None
    docs = None
    return dict(parent=parent,
                docs=docs,
                children=children)


def topic():
    '''
    List articles tagged with a particular blog_tags item.

    The first url argument should be the topic to be displayed, and can be
    either the row id number (int) or the tag name (string). If no argument
    is specified, provide an alphabetical list of links to all tags.
    '''
    try:
        # Is the argument an id or a name string?
        the_arg = request.args[0]
        if re.match(r'[1-9]+', the_arg):
            the_id = int(the_arg)
        else:
            the_id = db(db.blog_tags.tagname == the_arg).select().first().id

        tag_arts = db((db.articles.id == the_id) &
                      (db.articles.blog_tags.contains(the_id))
                      ).select(orderby=~db.articles.created)
        for a in tag_arts:
            if a.teaser == '':
                a.teaser = smart_truncate(a.body)
            a.author = '{} {}'.format(db.auth_user[a.author].first_name,
                                    db.auth_user[a.author].last_name)
        taglist = None

    except IndexError:
        tag_arts = None
        taglist = db().select(db.blog_tags.ALL)

    return dict(articles=tag_arts, taglist=taglist)
