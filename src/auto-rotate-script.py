#!/usr/bin/python
# coding: utf-8

import glob
from autorotate import AutoRotate

print "Start auto rotate script"
print "---------------------------------------------"
rot = AutoRotate()
target = "../rotate/*.tif"
count = 0
maxcount = len(glob.glob(target))
for f in glob.glob(target):
    count += 1
    try:
        log = rot.autorotate(f)
        print '(' + str(count) + '/' + str(maxcount) + ')' + "Success: " + f
        print log 
    except:
        print '(' + str(count) + '/' + str(maxcount) + ')' + "Error:   Unexpected error: " + f
        
print "---------------------------------------------"
print "Finish: " + str(count) + " items."
