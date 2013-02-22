#!/usr/bin/python
# coding: utf-8

import sys, os
import Image
from log import Log

class Image:
    def __init__(self):
        log.info = ['Image', '__init__', '', '']
        log.out()
    def crop(self, filename):
        log.info = ['Image', 'crop', [filename], '']
        today = datetime.today()
        tempname = today.strftime('%Y%m%d%H%M%S')
        im = Image.open(filename)
        x1 = int(im.size[0] * 0.8)
        y1 = int(im.size[1] * 0.8)
        x2 = im.size[0]
        y2 = im.size[1]
        box = (x1, y1, x2, y2)
        im.crop(box).save(tempname + '.gif')
        log.out()
    def splitMultiPages(self, filename):
        log.info = ['Image', 'splitMultiPages', [filename], '']
        im = Image.open(filename)
        try:
            count = 0
            while 1:
                im.seek(count)
                im.save(os.path.splitext(filename)[0] + "_%04d" % count + ".tif")
                count += 1
                log.comment = filename + ": Split (" + count + ") multi page type TIFF."
                log.out()
        except EOFError:
            log.comment = filename + ": Split error!"
            log.out()
            pass
