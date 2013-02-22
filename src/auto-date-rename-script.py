#!/usr/bin/python
# coding: utf-8
import glob, subprocess
from datetime import datetime

for f in glob.glob("content*.tif")
    today = datetime.today()
    dt = today.strftime('%Y%m%d%H%M%S%f')
    command = ['mv', f, dt + ".tif"]
    subprocess.call(command, stderr=subprocess.PIPE)
