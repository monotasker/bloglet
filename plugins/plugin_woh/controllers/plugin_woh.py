#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
File: plugin_woh.py.

Author: Me
Description:

"""

if 0:
    from gluon import SPAN, request, db, current, TAG
from pprint import pprint
import traceback
session = current.session


def get_nav_refs(chapnum, secnum, flatrefs):
    """docstring for get_nav_refs"""
    thisnode = flatrefs.index((int(chapnum), int(secnum)))
    prevnode = flatrefs[thisnode] if thisnode == 0 else flatrefs[thisnode - 1]
    nextnode = flatrefs[thisnode] if thisnode == len(flatrefs) + 1 else flatrefs[thisnode + 1]
    return prevnode, nextnode


def section():

    try:
        treeref, flatref = get_tree()
        chapnum = request.args[0] if request.args else sorted(treeref.keys())[0]
        secnum = request.args[1] if len(request.args) > 0 else treeref[chapnum][0]

        title1 = db.chapter_titles(db.chapter_titles.num == chapnum).title
        sec = db((db.section_titles.chapter_num == chapnum) &
                (db.section_titles.section_num == secnum)).select().first()
        try:
            title2 = sec.title
        except AttributeError:
            title2 = ''

        pars = db((db.paragraphs.chapter == chapnum) &
                  (db.paragraphs.section == secnum)
                  ).select(orderby=db.paragraphs.subsection)
        print 'found {} par rows'.format(len(pars))

        # nav data
        prevnode, nextnode = get_nav_refs(chapnum, secnum, flatref)

        # this section content
        paragraphs = []
        for p in pars:
            mypar = {}
            num = SPAN('.'.join([s for s in [str(chapnum), str(secnum),
                                             str(p.subsection)] if s]),
                       _class='woh-refnum')
            mypar['num'] = num
            mypar['text'] = TAG(p.body)
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

        return {'title1': title1,
                'title2': title2,
                'paragraphs': paragraphs,
                'prevref': prevnode,
                'treerefs': session.treerefs,
                'nextref': nextnode}
    except Exception:
        print traceback.format_exc(5)


def get_tree():
    """
    """
    paragraphs = db(db.paragraphs.id > 0).select(orderby=db.paragraphs.chapter | db.paragraphs.section)
    chapters = [p.chapter for p in paragraphs]
    chapters = sorted(list(set(chapters)))
    treerefs = {}
    flatrefs = []
    for c in chapters:
        sections = [int(p.section) for p in paragraphs.find(lambda r: r.chapter == c)]
        sections = sorted(list(set(sections)))
        treerefs[int(c)] = sections
        for s in sections:
            flatrefs.append((int(c), int(s)))
    pprint(treerefs)
    pprint(flatrefs)
    session.woh_treerefs = treerefs
    session.woh_flatrefs = flatrefs

    return treerefs, flatrefs


def read():
    """
    Set up reading environment for woh.
    """
    treerefs, flatrefs = get_tree()
    print 'reading'
    return {'treerefs': treerefs}
