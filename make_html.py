#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    make_html.py
    zergl <e3.gemini@qq.com>
    2015/07/18
'''

import os
import sys
import markdown as md   # from webpy/tools/markdown.py

def _md_2_html(mdfile = ""):
    html = md.Markdown(open(mdfile).read())
    filename = mdfile.replace(".md", ".html").replace(".markdown", ".html")
    with open(filename, 'w') as h:
        h.write(html)
        print "  --> translating: %s -> %s" %(mdfile, filename)
    
def _translate(mddir):
    for file in os.listdir(mddir):
        if file.endswith(".md") or file.endswith(".markdown"):
            _md_2_html(os.path.join(os.path.abspath(mddir), file))
            
if __name__ == '__main__':
    if len(sys.argv) == 2:
        _translate(sys.argv[1]);  
    else:
        print "\n  Usage:   python %s DIR-OF-MARKDOWN-FILES \n" %sys.argv[0]     