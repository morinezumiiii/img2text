#!/usr/bin/python
# -*- coding: utf-8 -*=
from datetime import datetime
class LogAssist:
    def getTime(self):
        today = datetime.today()
        dt = today.strftime('%Y%m%d%H%M%S')
        return dt
