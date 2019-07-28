#!/usr/bin/env python
import time

from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOW
def dependencies():
    pass
'''
update header time
Systemtime: 201907261118000
'''

def tamper(payload, **kwargs):
	Systemtime = (time.strftime("%Y%m%d%H%S000"))
	headers = kwargs.get("headers",{})
	headers["Systemtime"] = Systemtime
	return payload




