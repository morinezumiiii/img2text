#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, subprocess
import string, glob
import logging

from logassist import LogAssist
from mtime import mtime
from file import File
from imageedit import ImageEdit
from multipagetiff import MultiPageTiff
from tesseract import Tesseract
from loadtext import LoadText
from paper import Paper

# Arguments check
argvs = sys.argv
argc = len(argvs)
if (argc < 2):
    print 'argument error: please add arg[1]=filename'
    quit()
else:    
    target_file = "../image/" + argvs[1] 

# Initialize
print 'Initializing...'
timer = mtime()
log = LogAssist()
logfile = str(log.getTime()) + '.log'
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', \
                    datefmt='%Y/%m/%d %H:%M:%S', \
                    filename=logfile, level=logging.DEBUG)
logging.info('Start of Tiff image file corrective and file rename from Tesseract OCR')
logging.info('(Target file is ' + target_file + ')')
sh = File()
img = ImageEdit()
tif = MultiPageTiff()
ocr = Tesseract()
txt = LoadText()
paper = Paper()

image_dir = "../image/"
backup_dir = "../backup/"
rename_dir = "../rename/"
pass_dir = "../rename/pass/"
fail_dir = "../rename/fail/"
log_dir = "../rename/log/"

force = True
sh.mkdir(backup_dir, force)
sh.mkdir(image_dir, force)
sh.mkdir(rename_dir, force)
sh.mkdir(pass_dir, force)
sh.mkdir(fail_dir, force)
sh.mkdir(log_dir, force)
sh.mkdir("../rotate", force)
sh.mkdir("../rotate/pass", force)
sh.mkdir("../rotate/fail", force)
sh.mkdir("../rotate/log", force)
sh.mkdir("../check", force)
sh.mkdir("../check/pass", force)
sh.mkdir("../check/fail", force)

print 'Split multi page tiff files...'
logging.info('Split multi page tiff files')
files = glob.glob(target_file)
count = 0
for f in files:
    if tif.count(f) > 1:
        count += 1
        tif.split(f)
        os.remove(f)
        logging.info('('+ str(count) + ')' + 'split multipage tiff: ' + os.path.basename(f))
if count == 0:
    logging.info('Multi page tiff is not found.')

print 'Rename file from OCR Text...'
logging.info('Rename file from OCR Text')
success = 0
failed = 0
count = 0
files = glob.glob(target_file)
for f in files:
    count += 1
    print '(' + str(count) + '/' + str(len(files)) + '): ' + f
    logging.info('(' + str(count) + '/' + str(len(files)) + '): ' + f)

    b = os.path.basename(f)
    b,ext = os.path.splitext(b)
    basefile = b + ".tif"
    textfile = b + ".txt"
    tempfile = b + ".gif"
    outfile = ""

    sh.move(image_dir + basefile, rename_dir + basefile)
    sh.copy(rename_dir + basefile, backup_dir + basefile)
    logging.info('backup original tiff file: ' + basefile)

    r = img.autorotate(rename_dir + basefile)
    logging.info(r)
    img.convertTiffToGif(rename_dir + basefile)
    img.crop(rename_dir + tempfile)
    ocr.run_eng(rename_dir + tempfile)
    if txt.load(rename_dir + textfile):
        hit = True
    else:
        ocr.run_jpn(rename_dir + tempfile)
        if txt.load(rename_dir + textfile):
            hit = True
        else:
            hit = False
    if hit:
        logging.info('Text detect was success: ' + basefile + ' is ' + txt.result)
        existcount = sh.exist(pass_dir + txt.result + "*.tif")
        if existcount > 0:
            outfile = txt.result + "-" + str(existcount) + ".tif"
        else:
            outfile = txt.result + ".tif"
        sh.rename(rename_dir + basefile, rename_dir + outfile)
        logging.info('Rename file from paper size')
        p = paper.size(rename_dir + outfile)
        if p != 'Unknown':
            destfile = outfile[0:2] + str(p)[1:2] + outfile[3:16]
            if outfile != destfile: 
                sh.rename(rename_dir + outfile, rename_dir + destfile)
                logging.info('Paper size is ' + p + ' : ' + outfile + ' to ' + destfile)
                outfile = destfile
        else: 
            logging.warning('Paper size detect was not A0-A4 format.: ' + outfile)
        sh.move(rename_dir + textfile, log_dir + textfile)
        sh.move(rename_dir + outfile, pass_dir + outfile)
        sh.remove(rename_dir + tempfile)
        success += 1
    else:
        logging.warning('Can not detect text from OCR: ' + basefile)
        try:
            sh.move(rename_dir + textfile, fail_dir + textfile)
        except:
            pass
        try:
            sh.move(rename_dir + tempfile, fail_dir + tempfile)
        except:
            pass
        try:
            sh.move(rename_dir + basefile, fail_dir + basefile)
        except:
            pass
        failed += 1

if count == 0:
    logging.info('File not found. Rename process was nothing to do.')

print 'Auto correct and Finalize...'
logging.info('Auto correct and Finalize')
for f in glob.glob(pass_dir + "AN*.tif"):
    destfile = "AD" + f[2:12]
    sh.rename(f, pass_dir + destfile)
    logging.info('Auto correct file rename: ' + os.path.basename(f) + ' to ' + destfile)

for f in glob.glob(pass_dir + "AR*.tif"):
    destfile = "AK" + f[2:12]
    sh.rename(f, pass_dir + destfile)
    logging.info('Auto correct file rename: ' + os.path.basename(f) + ' to ' + destfile)

for f in glob.glob(pass_dir + "AX*.tif"):
    destfile = "AK" + f[2:12]
    sh.rename(f, pass_dir + destfile)
    logging.info('Auto correct file rename: ' + os.path.basename(f) + ' to ' + destfile)

timer.end()
print 'Finish! ' + \
  str(count) + ' items processed. ' + \
  '(Success: ' + str(success) + \
  ' Failed: ' + str(failed) + ')'
print 'Duration: ' + str(timer.duration())
logging.info('Finish of all operation. (duration ' + str(timer.duration()) + ')')
logging.info('Success: ' + str(success) + '/' + str(count))
logging.info('Failed : ' + str(failed) + '/' + str(count))
logging.shutdown()
