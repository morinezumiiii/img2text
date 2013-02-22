#/usr/bin/python
# -*- encoding=UTF-8 -*-
#プログラムの処理時間を計測するプログラム
# http://d.hatena.ne.jp/yosshi71jp/20090520/1242829279
import time;
class mtime:
    def __init__(self):
        self.start = time.time();
    def end(self):
        self.end = time.time();
    def duration(self):
        self.process = self.end - self.start;
        self.h = int(self.process / 3600);
        self.process -= self.h * 3600;
        self.m = int(self.process / 60);
        self.process -= self.m * 60;
        self.s = self.process;
        t = "time: %dh %dm %fs" % (self.h, self.m, self.s)
        return t;
