#!/usr/bin/python
# coding: utf-8

from imageedit import ImageEdit

im = ImageEdit()
degrees = float(im.getSlopeDegrees('test.gif',100))
print float(degrees)

im.rotate('test.gif', float(degrees))
