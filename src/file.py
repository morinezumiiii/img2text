#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, shutil, glob
class File:
    def mkdir(self, dir, force):
        if force:
            try:
                os.mkdir(dir)
            except OSError:
                pass
        else:
            os.mkdir(dir)
    def move(self, src, dst):
        os.rename(src, dst)
    def copy(self, src, dst):
        suffix = len(glob.glob(dst + '*'))
        if suffix > 0:
            suffix = '-' + str(suffix) + '.tif'
        else:
            suffix = ''
        shutil.copy(src, dst + suffix)
    def remove(self, file):
        os.remove(file)
    def rename(self, src, dst):
            os.rename(src, dst)
    def exist(self, file):
        count = 0
        for i in glob.glob(file):
            count += 1
        return count
    def count(self, file):
        count = 0
        for i in glob.glob(file):
            count += 1
        return count
