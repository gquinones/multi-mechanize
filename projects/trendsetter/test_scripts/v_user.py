
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
        resp = urllib2.urlopen('http://trendsetter.glgroup.com/')
        #print resp.code
        
        content = resp.read()
        #print content
        
        latency = time.time() - start_timer
        
        self.custom_timers['Trendsetter_Homepage'] = latency
        
        assert (resp.code == 200), 'Bad HTTP Response'
        assert ('Welcome to Trendsetter' in content), 'Welcome to Trendsetter'


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers