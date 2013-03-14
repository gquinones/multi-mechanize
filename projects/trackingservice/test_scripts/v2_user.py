#!/usr/bin/env python
#
#  Copyright (c) 2010 Corey Goldberg (corey@goldb.org)
#  License: GNU LGPLv3
#
#  This file is part of Multi-Mechanize


import urllib2
import time

class Transaction(object):
    def __init__(self):
        self.custom_timers = {}
    
    def run(self):
        start_timer = time.time()
        host = "http://10.115.100.203:4567/"
        urls = ["verification_employment/461138","verification_employment/21117","verification_employment/483188"]
        for url in urls:
            resp = urllib2.urlopen(host+url)
            print resp.code
        
            content = resp.read()
            assert (resp.code == 200), 'Bad HTTP Response'
            assert ('EmploymentId' in content), 'EmploymentId is missing'
            print content

        latency = time.time() - start_timer
        
        self.custom_timers['Verification'] = latency
        
        #assert (resp.code == 200), 'Bad HTTP Response'
        #assert ('Welcome to Trendsetter' in content), 'Welcome to Trendsetter'


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
