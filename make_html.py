#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    make_html.py
    zergl <e3.gemini@qq.com>
    2015/07/18

    - 2018/01/05 updated
'''

import os
import sys
import markdown as md   # from webpy/tools/markdown.py

def _md_2_html(mdfile = ""):
    html = md.Markdown(open(mdfile).read())
    filename = mdfile.replace(".md", ".html").replace(".markdown", ".html")
    with open(filename, 'w') as h:
        h.write(html)

def _list(_dir, _exclude_list):
    if not os.path.isdir(_dir):
        return []

    _items = []
    for file in os.listdir(_dir):
        if file in _exclude_list:
            continue

        _full_path = os.path.join(os.path.abspath(_dir), file)
        if os.path.isfile(_full_path):
            if file.endswith(".md") or file.endswith(".markdown"):
                html = _full_path.replace(".md", ".html").replace(".markdown", ".html")
                has_html = True if os.path.exists(html) else False
                _items.append([_full_path, has_html])
        else:
            _items.extend(_list(_full_path, _exclude_list))

    return _items

def _generate(mddir):
    _d = {} #for making index.html

    _exclude_list = [".git", "static"]
    _d = _list(mddir, _exclude_list)
    pwd = os.getcwd()
    print "PWD:", pwd
    for it in _d:
        file, has_html = it
        has_html = False
        if not has_html:
            _md_2_html(file)
            print "  --> Generating: %s -> %s" %(file, file.replace(".md", ".html").replace(".markdown", ".html"))

if __name__ == '__main__':
    _root_dir = './' if len(sys.argv) == 1 else sys.argv[1]
    _generate(_root_dir)

