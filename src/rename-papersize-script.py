#!/usr/bin/python
# coding: utf-8

import glob, subprocess
import Image

class Paper:
    def size(self, filename):
        im = Image.open(filename)
        width,height = im.size
        if width <= height:
            length = height
        else:
            length = width

        if 1000 <= length < 2500:
            size = 'A4'
        elif 2500 <= length < 4000:
            size = 'A3'
        elif 4000 <= length < 6000:
            size = 'A2'
        elif 6000 <= length < 8000:
            size = 'A1'
        elif 8000 <= length < 10000:
            size = 'A0'
        else:
            size = 'Unknown'

        return size

p = Paper()
for f in glob.glob('*.tif'):
    p.size(f)
    destfile = f[0:2] + str(p.size(f))[1:2] + f[3:16]
    if f != destfile:
        command = ('mv', f, destfile)
        subprocess.call(command)
