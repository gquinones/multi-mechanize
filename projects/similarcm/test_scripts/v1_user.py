
#!/usr/bin/env python
#
#  Copyright (c) 2010 Corey Goldberg (corey@goldb.org)
#  License: GNU LGPLv3
#
#  This file is part of Multi-Mechanize

import os.path
import sys
import random
import requests
import time


class Transaction(object):
    def __init__(self):
        self.custom_timers = {}
    
    def makeCall( self, url ):
        start_timer = time.time()
        r = requests.get(url)
    
        #content = r.text
        #print content
    
        latency = time.time() - start_timer
    
        self.custom_timers['similarcm_service'] = latency
    
        if latency > 5:
            writeErrorInfo('latency value of %f with %s' %(latency, url) )
        if r.status_code != 200:
            writeErrorInfo('status code with %s is %s' %(r.status_code, url) )
    
        assert (r.status_code == 200), 'Bad HTTP Response'
        assert ('foo' in r.text), 'No foo'
    
    def run(self):
        url = 'http://similarcm-dev.glgroup.com/recommend/consultrecsnorate?callback=foo&consultid=161115&cmid=580721&cmid=529311&cmid=597019&cmid=15646&cmid=153452&cmid=23646&cmid=45646'
        self.makeCall( url )
            
if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
