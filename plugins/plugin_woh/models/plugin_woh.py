#! /usr/bin/python
# -*- coding:utf-8 -*-

if 0:
    from gluon import Field, db
import datetime
#import os
now = datetime.datetime.utcnow()

db.define_table('chapter_titles',
                Field('uid', 'integer'),
                Field('num'),
                Field('title', 'string', length=512),
                format=lambda r: '{}: {}'.format(r.num, r.title)
                )

db.define_table('section_titles',
                Field('uid', 'integer'),
                Field('chapter_num', 'list:reference chapter_titles'),
                Field('section_num'),
                Field('title', 'string', length=512),
                format=lambda r: '{}.{}: {}'.format(r.chapter_num,
                                                    r.section_num, r.title)
                )

db.define_table('woh_audio',
                Field('uid', 'integer'),
                Field('audio_title', length=512),
                Field('audio_description', 'text'),
                Field('audio_file_mp3', 'upload', length=256,
                      uploadfolder='static/audio'),
                Field('audio_file_ogg', 'upload', length=256,
                      uploadfolder='static/audio'),
                format=lambda r: r.audio_title
                )

db.define_table('woh_images',
                Field('uid', 'integer'),
                Field('image_title', length=512),
                Field('image_description', 'text'),
                Field('img_file', 'upload', length=256,
                      uploadfolder='static/images'),
                format=lambda r: r.audio_title
                )

db.define_table('paragraphs',
                Field('uid', 'integer'),
                Field('chapter', 'string', length=512),
                Field('chapter_id', 'reference chapter_titles'),
                Field('section', 'string'),
                Field('subsection', 'string'),
                Field('display_title'),
                Field('status', 'string'),
                Field('created'),  # 'datetime', default = now
                Field('changed'),  # 'datetime', default = now
                Field('body', 'text'),
                Field('pullquote', 'string', length=512),
                Field('audio', 'list:reference woh_audio'),
                Field('image', 'list:reference woh_images'),  # 'list:reference woh_images'
                Field('topics'),
                format=lambda r: '{}, {}, {}'.format(r.chapter, r.section, r.subsection)
                )

db.define_table('topics',
                Field('uid', 'integer'),
                Field('topic', 'string', length=512),
                format=lambda r: r.topic
                )
