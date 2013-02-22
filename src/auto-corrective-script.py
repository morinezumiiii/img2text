#!/usr/bin/python
# coding: utf-8

import glob, subprocess

for f in glob.glob('AN*.tif'):
    destfile = 'AD' + f[2:12]
    command = ['mv', f, destfile]
    subprocess.call(command)

for f in glob.glob('AR*.tif'):
    destfile = 'AK' + f[2:12]
    command = ['mv', f, destfile]
    subprocess.call(command)

for f in glob.glob('AX*.tif'):
    destfile = 'AK' + f[2:12]
    command = ['mv', f, destfile]
    subprocess.call(command)
