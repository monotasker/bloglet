db.define_table('plugin_comments_comment',
    Field('body','text', label='Your comment'),
    Field('posted_on', 'datetime', default=request.now),
    Field('posted_by', db.auth_user, default=auth.user_id))
db.plugin_comments_comment.posted_on.writable=False
db.plugin_comments_comment.posted_on.readable=False
db.plugin_comments_comment.posted_by.writable=False

db.plugin_comments_comment.posted_by.readable=False

def plugin_comments():
    return LOAD('plugin_comments','post.load',ajax=True, _class="comments")
