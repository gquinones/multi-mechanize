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
        urls = ["http://10.45.205.242:4567/callpcts/760","http://10.45.205.242:4567/callpcts/360","http://10.45.205.242:4567/callpcts/900"]
        for url in urls:
            resp = urllib2.urlopen(url)
            #print resp.code
        
            content = resp.read()
            assert (resp.code == 200), 'Bad HTTP Response'
            assert ('Supporting Data' in content), 'Supporting Data not seen'
        #print content

        latency = time.time() - start_timer
        
        self.custom_timers['Callpcts'] = latency
        
        #assert (resp.code == 200), 'Bad HTTP Response'



if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
