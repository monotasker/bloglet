# -*- coding: utf-8 -*-
if 0:
    from gluon import DAL, URL

from gluon.tools import Auth, Mail, Crud, Service, PluginManager
from gluon.tools import Recaptcha
from gluon.globals import current
response = current.response
request = current.request

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

db = DAL('sqlite://storage.sqlite')
current.db = db

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
#response.optimize_css = 'concat,minify,inline'
#response.optimize_js = 'concat,minify,inline'

#configure authorization
auth = Auth(db, hmac_key=Auth.get_or_create_key())  # authent/authorization
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables()

# get private data from secure file
keydata = {}
with open('applications/paideia/private/app.keys', 'r') as keyfile:
    for line in keyfile:
        k, v = line.split()
        keydata[k] = v

#configure mail
mail = Mail()                                  # mailer
mail.settings.server = keydata['email_sender'] or 'logging'  # SMTP server
mail.settings.sender = keydata['email_address']  # email
mail.settings.login = keydata['email_pass']  # credentials or None

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = True
auth.settings.reset_password_requires_verification = True
auth.messages.verify_email = 'Click on the link http://' \
    + request.env.http_host + URL('default', 'user', args=['verify_email']) \
    + '/%(key)s to verify your email'
auth.settings.reset_password_requires_verification = True
auth.messages.reset_password = 'Click on the link http://' \
    + request.env.http_host + URL('default', 'user', args=['reset_password'])\
    + '/%(key)s to reset your password'
#place auth in current so it can be imported by modules
current.auth = auth

#enable recaptcha anti-spam for selected actions
auth.settings.login_captcha = None
auth.settings.register_captcha = Recaptcha(request,
    keydata['captcha_public_key'], keydata['captcha_private_key'])
auth.settings.retrieve_username_captcha = Recaptcha(request,
    keydata['captcha_public_key'], keydata['captcha_private_key'])
auth.settings.retrieve_password_captcha = Recaptcha(request,
    keydata['captcha_public_key'], keydata['captcha_private_key'])

crud.settings.auth = None        # =auth to enforce authorization on crud
