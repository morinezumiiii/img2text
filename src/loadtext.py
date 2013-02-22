#!/usr/bin/python
# -*- coding: utf-8 -*-
import string, re
result = ''
class LoadText:
    def load(self, filename):
        self.filename = filename
        f = open(self.filename, 'r')
        data = f.read()
        f.close()
        lines = data.split('\n')
        s = ''
        for line in lines:
            s = s + line
        s = string.replace(s,'e','6')
        s = string.upper(s)
        s = string.replace(s,'1-1','H')
        s = string.replace(s,'1-I','H')
        s = string.replace(s,'I-1','H')
        s = string.replace(s,'I-I','H')
        s = string.replace(s,'}1','H')
        s = string.replace(s,'}I','H')
        s = string.replace(s,'1-T','F')
        s = string.replace(s,'1-"','F')
        s = string.replace(s,'S','8')
        s = string.replace(s,'Q','0')
        s = string.replace(s,'O','0')
        s = string.replace(s,'Z','2')
        s = string.replace(s,'I','1')
        s = string.replace(s,' ','')
        s = string.replace(s,',','')
        s = string.replace(s,'.','')
        s = string.replace(s,"'",'')
        s = string.replace(s,'"','')
        s = string.replace(s,'-','')
        s = string.replace(s,'_','')
        s = string.replace(s,'ﾂｧ','')
        s = string.replace(s,' ','')
        prog = re.compile('[A-Z][A-Z]\d{6}')
        result = prog.search(s)
        if result:
            self.result = result.group(0)
            return True
        else:
            self.result = ''
        return False
