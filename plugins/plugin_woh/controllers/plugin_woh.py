#! /usr/bin/python
# -*- coding:utf-8 -*-

if 0:
    from gluon import SPAN, request, db, H1, H2
from pprint import pprint
import traceback


def section():
    try:
        chapnum = request.args[0] if request.args[0] else 0
        secnum = request.args[1] if request.args[0] else 0
        pars = db((db.paragraphs.chapter == chapnum) &
                  (db.paragraphs.section == secnum)
                  ).select(orderby=db.paragraphs.subsection)
        print 'found {} par rows'.format(len(pars))
        paragraphs = []
        for p in pars:
            mypar = {}
            num = SPAN('.'.join([s for s in [str(chapnum), str(secnum),
                                             str(p.subsection)] if s]),
                       _class='woh-refnum')
            mypar['num'] = num
            mypar['text'] = p.body
            if p.audio:
                for a in p.audio:
                    mypar['auds'] = []
                    arow = db.woh_audio(a)
                    mypar['auds'].append((arow.audio_title,
                                          arow.audio_description,
                                          arow.audio_file_mp3,
                                          arow.audio_file_ogg))
            else:
                mypar['auds'] = None

            if p.image:
                for i in p.image:
                    mypar['images'] = []
                    irow = db.woh_images(i)
                    mypar['images'].append((irow.img_title,
                                            irow.image_description,
                                            irow.img_file))
            else:
                mypar['images'] = None

            paragraphs.append(mypar)

        pprint(paragraphs)
        return {'paragraphs': paragraphs}
    except Exception:
        print traceback.format_exc(5)


def read():
    chapnum = request.args[0] if request.args[0] else 0
    secnum = request.args[1] if request.args[1] else 1
    title1 = H1(db.chapter_titles(db.chapter_titles.num == chapnum).title)
    sec = db((db.section_titles.chapter_num == chapnum) &
             (db.section_titles.section_num == secnum)).select().first()
    try:
        title2 = H2(sec.title)
    except AttributeError:
        title2 = ''
    print 'reading'
    return {'title1': title1, 'title2': title2,
            'chapnum': chapnum, 'secnum': secnum}
