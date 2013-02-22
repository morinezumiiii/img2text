#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os, subprocess, string
import Image
import math
debugmode = False
convert_path = ""
class ImageEdit:
    def __init__(self):
        if sys.platform == 'win32':
            self.convert_path = "C:\Program Files\ImageMagick-6.7.9-Q16\convert.exe"
        else:
            self.convert_path = "convert"
    def getPortrait(self,size):
        w,h = size
        if w > h:
            return 'horizontal'
        else:
            return 'vertical' 
    def crop(self, filename):
        im = Image.open(filename)
        if self.getPortrait(im.size) == 'horizontal':
            x1 = int(im.size[0] * 0.78)
            y1 = int(im.size[1] * 0.82)
        else:
            x1 = int(im.size[0] * 0.55)
            y1 = int(im.size[1] * 0.84)
        x2 = im.size[0]
        y2 = im.size[1]
        box = (x1, y1, x2, y2)
        im.crop(box).save(filename)
    def convertTiffToGif(self, filename):
        base,ext = os.path.splitext(filename)
        command = [self.convert_path, filename, base + ".gif"]
        subprocess.call(command, stderr=subprocess.PIPE)
        return base + ".gif"
    def getSlopeDegrees(self, filename, precision):
        im = Image.open(filename)
        rgb = im.convert('RGB')
        w,h = im.size
        d = math.trunc(w / precision)
        if debugmode:
            print 'detect point interval: ' + str(d)
        hitlimit = 3
        tolerance = 50
        isdetected = False
        for x in range(0, w-1 ,d):
            for y in range(h-1, 0, -1):
                if rgb.getpixel((x, y)) == (0, 0, 0):
                    hit += 1
                    if hit == hitlimit:
                        if not isdetected:
                            isdetected = True
                            firstx = x
                            firsty = y
                            y2 = y
                        # TODO Don't get avarage value! fix it another method.
                        #y2 = (y2 + y) / 2
                        if abs(y2 - y) > tolerance:
                            if debugmode:
                                print 'detected pixel is invalid: (' + str(x) + ',' + str(y) + ')'
                            break
                        else:
                            x2 = x
                            y2 = y
                            if debugmode:
                                print 'detected pixel at: (' + str(x) + ',' + str(y) + ')'
                            break
                else:
                    hit = 0
            if hit == 0:
                if debugmode:
                    print 'dose not detected pixel: (' + str(x) +')'
            hit = 0
        base = x2 - firstx
        height = y2 - firsty
        if float(base) == 0:
            base = 1
        rad = (math.tan(float(height) / float(base))) * -1
        degrees = math.degrees(rad)
        if debugmode:
            print 'first x,y: ' + str(firstx) + ',' + str(firsty)
            print 'last x,y: ' + str(x2) + ',' + str(y2)
            print 'base: ' + str(base) + ' height: ' + str(height)
            print 'rad: ' + str(rad) + ' degrees: ' + str(degrees)
        return degrees
    def rotate(self, filename, degrees):
        command = [self.convert_path, filename, \
                   '-rotate', str(degrees), \
                   '-alpha', 'Deactivate', \
                   '-background','white', \
                   filename]
        subprocess.call(command, stderr=subprocess.PIPE)
    def autorotate(self, src):
        tmp = self.convertTiffToGif(src)
        width, height = Image.open(tmp).size
        size = str(width) + 'x' + str(height)
        if debugmode:
            print 'temporary file is: ' + tmp + ' [' + size + ']'
        degrees = self.getSlopeDegrees(tmp, 10)
        if debugmode:
            print 'slope degree is: ' + str(degrees)
        command = ['rm', tmp]
        subprocess.call(command, stderr=subprocess.PIPE)
        command = [self.convert_path, src, \
                   '-rotate', str(degrees), \
                   '-crop', str(size), \
                   src]
        subprocess.call(command, stderr=subprocess.PIPE)
        log = 'command: ' + string.join(command)
        return log
