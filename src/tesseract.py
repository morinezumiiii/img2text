#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, subprocess
class Tesseract:
    def run_eng(self, filename):
        self.filename = filename
        base,ext = os.path.splitext(filename)
        command = ['tesseract', self.filename, base, '-l', 'eng', '-psm', '6']
        subprocess.call(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    def run_jpn(self, filename):
        self.filename = filename
        base,ext = os.path.splitext(filename)
        command = ['tesseract', self.filename, base, '-l', 'jpn', '-psm', '6']
        subprocess.call(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
