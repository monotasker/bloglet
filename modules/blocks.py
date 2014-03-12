from gluon import UL, LI, A, URL


def get_block(myblock):
    """
    """
    tynprox = 'http://ezproxy.mytyndale.ca:2048/login?url='
    chicago = 'http://www.chicagomanualofstyle.org.ezproxy.mytyndale.ca:2048/'
    sacont = UL(LI(A('Tyndale Registrar',
                    _href='http://tyndale.ca/registrar')),
                LI(A('Tyndale Library',
                    _href='http://tyndale.ca/library')),
                LI(A('Chicago Style Quick Guide',
                    _href='{}{}tools_citationguide.html'.format(tynprox, chicago))),
                LI(A('Chicago Manual of Style',
                     _href='{}{}16/contents.html'.format(tynprox, chicago)),
                   ' (esp. ',
                   A(' ch. 14 ',
                     _href='{}{}16/ch14/ch14_toc.html'.format(tynprox, chicago)),
                   ' and sections ',
                   A('10.46 to 10.51',
                     _href='{}{}16/ch10/ch10_sec046.html'.format(tynprox, chicago)),
                   ', ',
                   A('14.253 to 14.254',
                     _href='{}{}16/ch14/ch14_sec253.html'.format(tynprox, chicago)),
                   ')'
                   )
                )
    classcont = UL(LI(A('New Testament Theology and History',
                        _href=URL('plugin_blog', 'classes', args=4))),
                   LI(A('New Testament Theology and History (Online)',
                        _href=URL('plugin_blog', 'classes', args=15))),
                   LI(A('Romans',
                        _href=URL('plugin_blog', 'classes', args=2))),
                   LI(A('Gospel of John',
                        _href=URL('plugin_blog', 'classes', args=17))),
                   LI(A('Elementary Greek I (Online)',
                        _href=URL('plugin_blog', 'classes', args=18))),
                   LI(A('Elementary Greek II (Online)',
                        _href=URL('plugin_blog', 'classes', args=16))),
                   LI(A('Jewish World of the NT',
                        _href=URL('plugin_blog', 'classes', args=13))),
                   )
    infocont = UL(LI('Associate Professor of New Testament at Tyndale Seminary in Toronto, Canada.'),
                  LI(A('iscott@tyndale.ca', _href='mailto:iscott@tyndale.ca')),
                  LI(A('Curriculum Vitae', _href='')),
                  )
    hourscont = UL(LI('Winter 2014'),
                   LI('Mon 3:30 - 6:00 pm'),
                   LI('Thurs 1:30 - 3:30 pm'),
                   LI('or by appointment')
                   )
    sitescont = UL(LI(A('Paideia', _href="http://ianwscott.webfactional.com/paideia")),
                   LI(A('Witnesses of Hope', _href=URL('plugin_woh', 'read', args=[0, 1]))),
                   LI(A('Missio Dei', _href="http://www.tyndale.ca/~missiodei")),
                   LI(A('The Online Critical Pseudepigrapha', _href="http://ocp.tyndale.ca")),
                   LI(A('Peergrades', _href="http://ianwscott.webfactional.com/peergrades"))
                   )
    socialcont = UL(LI(A('Github', _href="http://github.com/monotasker")),
                    LI(A('Flickr', _href="http://www.flickr.com/photos/ian-w-scott/")),
                    LI(A('Google+', _href="https://plus.google.com/u/0/100103028069838784737")),
                    LI(A('Academia.edu', _href="http://tyndale.academia.edu/IanScott")),
                    LI(A('Zotero', _href="https://www.zotero.org/iscott")),
                    LI(A('Twitter (@ianwscott)', _href="https://twitter.com/ianwscott")),
                    LI(A('Twitter (@the_monotasker)', _href="https://twitter.com/the_monotasker"))
                    )
    blocks = {'student_aids': {'blocktitle': 'General Student Aids',
                               'content': sacont},
              'classes': {'blocktitle': 'Classes',
                          'content': classcont},
              'info': {'blocktitle': 'Ian W. Scott, PhD',
                       'content': infocont},
              'hours': {'blocktitle': 'Office Hours',
                        'content': hourscont},
              'my_sites': {'blocktitle': 'My Sites',
                          'content': sitescont},
              'social': {'blocktitle': 'Me On the Web',
                         'content': socialcont},
              }
    theblock = blocks[myblock]
    return theblock
