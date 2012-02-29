# -*- coding: utf8 -*-

import fileinput
import re

_lineRegex = re.compile(r'(\d+\.\d+\.\d+\.\d+) ([^ ]*) ([^ ]*) \[([^\]]*)\] "([^"]*)" (\d+) ([^ ]*) "([^"]*)" "([^"]*)"')

class ApacheLogRecord(object):
  
    def __init__(self, * rgroups):
        self.ip, self.ident, \
        self.http_user, self.time, \
        self.request_line, self.http_response_code, \
        self.http_response_size, self.referrer, self.user_agent = rgroups
        self.http_method, self.url, self.http_vers = self.request_line.split()
    
    def __str__(self):
        return ' '.join([self.ip, self.ident, self.time, self.request_line, self.http_response_code, self.http_response_size, self.referrer, self.user_agent])

class ApacheLogFile(object):
  
    def __init__(self, * filename):
        self.f = fileinput.input(filename)
  
    def close(self):
        self.f.close()

    def __iter__(self):
        match = _lineRegex.match
        for line in self.f:
            m = match(line)
            if m:
                try:
                    log_line = ApacheLogRecord(*m.groups())
                    yield log_line
                except GeneratorExit:
                    pass
                except Exception as e:
                    print " NON_COMPLIANT_FORMAT: " , line, " Exception: " , e
