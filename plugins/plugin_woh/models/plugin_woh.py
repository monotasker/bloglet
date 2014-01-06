#! /usr/bin/python
# -*- coding:utf-8 -*-

import datetime

db.define_table('chapter_titles',
                Field('num', 'integer'),
                Field('title', 'string'),
                format=lambda r: '{}: {}'.format(r.num, r.title)
                )


db.define_table('section_titles',
                Field('chapter_num', 'integer'),
                Field('section_num', 'integer'),
                Field('title', 'string'),
                format=lambda r: '{}.{}: {}'.format(r.chapter_num,
                                                    r.section_num, r.title)
                )

db.define_table('paragraphs',
                Field('uid', 'integer'),
                Field('chapter', 'string'),
                Field('section', 'string'),
                Field('subsection', 'string'),
                Field('display_title'),
                Field('status', 'string'),
                Field('created'), #'datetime', default = datetime.datetime.utcnow()
                Field('changed'),
                Field('body', 'text'),
                Field('pullquote'),
                Field('audio', 'integer'),
                Field('image_id', 'integer'),
                Field('image_alt'),
                Field('image_title'),
                Field('image_filename'),
                Field('topics')
                )

