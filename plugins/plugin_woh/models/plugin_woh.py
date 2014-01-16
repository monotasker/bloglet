#! /usr/bin/python
# -*- coding:utf-8 -*-

if 0:
    from gluon import Field, db
import datetime
#import os
now = datetime.datetime.utcnow()

db.define_table('chapter_titles',
                Field('num'),
                Field('title'),
                format=lambda r: '{}: {}'.format(r.num, r.title)
                )

db.define_table('section_titles',
                Field('chapter_num'),
                Field('section_num'),
                Field('title', 'string'),
                format=lambda r: '{}.{}: {}'.format(r.chapter_num,
                                                    r.section_num, r.title)
                )

db.define_table('woh_audio',
                Field('audio_title'),
                Field('audio_description'),
                Field('audio_file_mp3', 'upload',
                      uploadfolder='static/audio'),
                Field('audio_file_ogg', 'upload',
                      uploadfolder='static/audio'),
                format=lambda r: r.audio_title
                )

db.define_table('woh_images',
                Field('image_title'),
                Field('image_description'),
                Field('img_file', 'upload',
                      uploadfolder='static/images'),
                format=lambda r: r.audio_title
                )

db.define_table('paragraphs',
                Field('uid', 'integer'),
                Field('chapter', 'string'),
                Field('chapter_id', 'reference chapter_titles'),
                Field('section', 'string'),
                Field('section_id', 'reference section_titles'),
                Field('subsection', 'string'),
                Field('display_title'),
                Field('status', 'string'),
                Field('created'),  # 'datetime', default = now
                Field('changed'),  # 'datetime', default = now
                Field('body', 'text'),
                Field('pullquote'),
                Field('audio'),  # 'list:reference woh_audio'
                Field('image'),  # 'list:reference woh_images'
                Field('topics'),
                format=lambda r: '{}, {}, {}'.format(r.chapter, r.section, r.subsection)
                )
