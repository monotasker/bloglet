#! /usr/bin/python
# -*- coding:utf-8 -*-

if 0:
    from gluon import SPAN
from os import path
import csv
import re
from pprint import pprint
import traceback
import datetime

def section():
    try:
        print 'starting section'
        chapnum = request.args[0] if request.args[0] else 0
        secnum = request.args[1] if request.args[0] else 0
        print 'chapter', chapnum
        print 'section', secnum
        pars = db((db.paragraphs.chapter == chapnum) &
                  (db.paragraphs.section == secnum)).select(orderby = db.paragraphs.subsection)
        print 'found {} paragraphs'.format(len(pars))
        txt = DIV()
        for p in pars:
            num = SPAN('.'.join([str(chapnum), str(secnum), str(p.subsection)]),
                    _class='woh-refnum')
            myp = P(num, p.body)
            txt.append(myp)
        return {'text': txt}
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

def woh_import():
    try:
        db.paragraphs.truncate()
    except:
        print traceback.format_exc(5)
    mydir = '/home/ian/Dropbox/Downloads/Webdev/woh_export'
    files = [
             'node-export(43-nodes).1335558252.csv',
             'node-export(50-nodes).1335557844.csv',
             'node-export(50-nodes).1335557890.csv',
             'node-export(50-nodes).1335557934.csv',
             'node-export(50-nodes).1335558015.csv',
             'node-export(50-nodes).1335558056.csv',
             'node-export(50-nodes).1335558115.csv',
             'node-export(50-nodes).1335558151.csv',
             'node-export(50-nodes).1335558186.csv'
             ]
    #'node-export[](1-nodes).1335557290.export',
    fullfiles = [path.join(mydir, f) for f in files]

    for ff in fullfiles:
        with open(ff, 'rU') as csfile:
            rows = csv.DictReader(csfile)
            for row in rows:
                #pprint(row)
                titlebits = row['title'].split('.') if row['title'] else [None, None, None]
                taxes = [v for k, v in row.iteritems()
                         if re.match(r'.*taxonomy.*', k)
                         and v not in ['NULL', '', 0, 'None', None]]
                topics = '|'.join(taxes) if taxes else None
                pullquote = row['field_pullquote[\'0\'][\'value\']'] \
                        if 'field_pullquote[\'0\'][\'value\']' in row.values() \
                        else None
                audio = row['field_audiolink[\'0\'][\'value\']'] \
                        if 'field_audiolink[\'0\'][\'value\']' in row.values() \
                        else None
                image_id = row['field_images[\'0\'][\'fid\']'] \
                        if 'field_images[\'0\'][\'fid\']' in row.values() \
                        else None
                image_alt = row['field_images[\'0\'][\'data\'][\'alt\']'] \
                        if 'field_images[\'0\'][\'data\'][\'alt\']' \
                        in row.values() else None
                image_title = row['field_images[\'0\'][\'data\'][\'title\']'] \
                        if 'field_images[\'0\'][\'data\'][\'title\']' \
                        in row.values() else None
                image_filename = row['field_images[\'0\'][\'filename\']'] \
                        if 'field_images[\'0\'][\'filename\']' in row.values() \
                        else None
                times = {}
                for k in ['changed', 'created']:
                    errors = 0
                    try:
                        times[k] = datetime.datetime.fromtimestamp(int(row[k]))
                    except (TypeError, ValueError):
                        times[k] = datetime.datetime.utcnow()
                        errors += 1
                    print '{} errors: {}'.format(k, errors)

                matches = {'uid': row['uid'],
                           'chapter': titlebits[0],
                           'section': titlebits[1] if len(titlebits) > 1 else 0,
                           'subsection': titlebits[2] if len(titlebits) > 1 else 0,
                           'display_title': row['field_displaytitle[\'0\'][\'value\']'],
                           'status': row['status'],
                           'changed': times['changed'],
                           'created': times['created'],
                           'body': row['body'],
                           'pullquote': pullquote,
                           'audio': audio,
                           'image_id': image_id,
                           'image_alt': image_alt,
                           'image_title': image_title,
                           'image_filename': image_filename,
                           'topics': topics}
                matches = {k: v for k, v in matches.iteritems() if not v in [None, 'NULL']}
                num = db.paragraphs.insert(**matches)
                print num

