#!/usr/bin/python
# -*- coding: utf-8 -*-
import glob, subprocess, os
import Image
from file import File
class MultiPageTiff:
    log = ""
    def count(self, filename):
        im = Image.open(filename)
        try:
            count = 0
            while 1:
                im.seek(count)
                count += 1
        except EOFError:
            self.log = "Error"
        return count
    def split(self, filename):
        sh = File()
        if self.count(filename) > 1:
            base,ext = os.path.splitext(filename)
            command = ["tiffsplit",filename]
            subprocess.call(command, stderr=subprocess.PIPE)
            count = 0
            for f in glob.glob("x*.tif"):
                sh.rename(f, base + "-" + str(count) + ext)
                count += 1
            sh.remove(filename)
            self.log = "Split multi page TIFF: " + f
