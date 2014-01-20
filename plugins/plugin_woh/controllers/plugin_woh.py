#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
File: plugin_woh.py.

Author: Me
Description:

"""

if 0:
    from gluon import request, db, current, TAG
    session = current.session
    response = current.response
from pprint import pprint
import traceback


def get_nav_refs(chapnum, secnum, flatrefs):
    """docstring for get_nav_refs"""
    thisnode = flatrefs.index((int(chapnum), int(secnum)))
    prevnode = flatrefs[thisnode] if thisnode == 0 else flatrefs[thisnode - 1]
    nextnode = flatrefs[thisnode] if thisnode == len(flatrefs) + 1 else flatrefs[thisnode + 1]
    return prevnode, nextnode


def section():

    try:
        treerefs, flatrefs = get_tree()
        chapnum = request.args[0] if request.args else sorted(treerefs.keys())[0]
        currsec = request.args[1] if len(request.args) > 0 else treerefs[chapnum][0]

        title1 = db.chapter_titles(db.chapter_titles.num == chapnum).title

        pars = db(db.paragraphs.chapter == chapnum
                  ).select(orderby=db.paragraphs.section | db.paragraphs.subsection)

        prevnode, nextnode = get_nav_refs(chapnum, currsec, flatrefs)

        secrows = db(db.section_titles.chapter_num == chapnum).select()
        sectitles = {s.section_num: s.title for s in secrows}

        sections = {}
        for mysec in treerefs[int(chapnum)]:
            paragraphs = []
            print 'found', len(pars)
            secpars = pars.find(lambda r: r.section == str(mysec))
            print 'secpars', len(secpars)
            for p in secpars:
                mypar = {}
                num = '.'.join([s for s in [str(chapnum), str(mysec),
                                            str(p.subsection)] if s])
                mypar['num'] = num
                mypar['par_title'] = p.display_title
                mypar['text'] = TAG(p.body)
                print 'parsed text for', num
                mypar['auds'] = get_audio(p)
                mypar['images'] = get_images(p)
                paragraphs.append(mypar)
            sections[mysec] = paragraphs

        return {'title1': title1,
                'sections': sections,
                'sectitles': sectitles,
                'prevref': prevnode,
                'treerefs': session.treerefs,
                'nextref': nextnode,
                'currsec': currsec}
    except Exception:
        print traceback.format_exc(5)


def download():
    """
    Display media file from upload field.
    """
    return response.download(request, db)


def get_audio(row):
    """
    Return a list of tuples with data on an audio file related to the row.
    """
    if row.audio:
        auds = [(db.woh_audio(a).audio_title,
                 db.woh_audio(a).audio_description,
                 db.woh_audio(a).audio_file_mp3,
                 db.woh_audio(a).audio_file_ogg)
                for a in row.audio]
    else:
        auds = None

    return auds


def get_images(row):
    """
    Return a list of tuples, each holding data on an image related to the row.
    """
    if row.image:
        imgs = [(db.images(i).img_title,
                 db.images(i).image_description,
                 db.images(i).img_file)
                for i in row.image]
    else:
        imgs = None

    return imgs


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
    #pprint(flatrefs)
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
