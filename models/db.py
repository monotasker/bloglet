# -*- coding: utf-8 -*-

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate, Recaptcha

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

db = DAL('sqlite://storage.sqlite')

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
#response.optimize_css = 'concat,minify,inline'
#response.optimize_js = 'concat,minify,inline'

auth = Auth(db, hmac_key=Auth.get_or_create_key())
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables()

## configure email
mail=auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'emailhere'
mail.settings.login = 'emailhere:passwordhere'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## configure captcha
auth.settings.login_captcha = None
auth.settings.register_captcha = Recaptcha(request, 
                                           '6Ldy5ccSAAAAALlI2gJuwFQYe-iaZ_oyQs3nhX-9', 
                                           '6Ldy5ccSAAAAABr8FhJeb_aELfEC7SJOOyvhJp0R')
auth.settings.retrieve_username_captcha = Recaptcha(request, 
                                           '6Ldy5ccSAAAAALlI2gJuwFQYe-iaZ_oyQs3nhX-9', 
                                           '6Ldy5ccSAAAAABr8FhJeb_aELfEC7SJOOyvhJp0R')
auth.settings.retrieve_password_captcha = Recaptcha(request, 
                                           '6Ldy5ccSAAAAALlI2gJuwFQYe-iaZ_oyQs3nhX-9', 
                                           '6Ldy5ccSAAAAABr8FhJeb_aELfEC7SJOOyvhJp0R')