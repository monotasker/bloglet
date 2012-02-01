# coding: utf8
if 0:
    from gluon import current
    from gluon.tools import Crud
    db, auth = current.db, current.auth
    crud = Crud(db)

#checks to see whether hidden 'honeypot' field has any text in it (presumably placed there by a bot)
def checkfilter(form):
    form.vars.filter = request.vars.filter
    if form.vars.filter == '':
        pass
    else:
        form.errors.bot = 'It seems like you may not be a human being! \
        If you are, be sure not to enter anything into any fields in the \
        form other than the large box for the text of your comment.'

def post():
    comment = db.plugin_comments_comment
    form = SQLFORM(comment, submit_button = 'add comment', separator = '', formstyle = 'ul', hidden = dict(filter = ''))
    # process form
    if form.process(onvalidation = checkfilter).accepted:
        response.flash = 'Thanks for your thoughts!'
    elif form.errors.bot:
        response.flash = form.errors.bot
    elif form.errors:
        response.flash = 'Sorry, something went wrong when I tried to add your comment.'
    else:
        pass

    comments = db(comment).select()
    return dict(form = form, comments = comments)
