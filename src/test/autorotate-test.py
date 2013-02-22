#!/usr/bin/python
# coding: utf-8

import subprocess
from autorotate import AutoRotate

basefile = 'test.tif'
destfile = 'testresult.tif'

command = ['cp', basefile, destfile]
subprocess.call(command)

rot = AutoRotate()
rot.autorotate(destfile)
