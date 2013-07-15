
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
    
    def writeErrorInfo(self, myInfo):
    
        basepath = os.path.dirname(__file__)
        fileTarget = os.path.join(basepath, "testinfo.txt")

        try:
            logfile = open(fileTarget, "a")
            print >> logfile, myInfo
            logfile.close()
        except Exception, err:
            sys.stderr.write('ERROR: %s\n' % str(err))
            sys.exit()
            
    def getConsultID(self):
        return random.randrange(1600000, 1688915)
        
    def getCMIDList(self):
        numtoget = random.randrange(5,20)
        #numtoget = 5
        cmidList=""
        for mynum in range(numtoget):
            cmid = random.randrange(500000, 590000)
            cmidList = cmidList + '&cmid=' + str(cmid)
        return cmidList
            
    
    def makeCall( self, url ):
        start_timer = time.time()
        r = requests.get(url)
    
        #content = r.text
        #print content
    
        latency = time.time() - start_timer
    
        self.custom_timers['similarcm_service'] = latency
    
        if latency > 5:
            self.writeErrorInfo('latency value of %f with %s' %(latency, url) )
        if r.status_code != 200:
            self.writeErrorInfo('status code with %s is %s' %(r.status_code, url) )
    
        assert (r.status_code == 200), 'Bad HTTP Response'
        assert ('foo' in r.text), 'No foo'
    
    def run(self):
        consultID = str(self.getConsultID())
        cmidList = self.getCMIDList()
        #print consultID
        url = 'http://similarcm.glgroup.com/recommend/consultrecsnorate?callback=foo&consultid=' + consultID + cmidList
        #url = 'http://similarcm-dev.glgroup.com/recommend/consultrecsnorate?callback=foo&consultid=' + consultID + cmidList
        #url = 'http://10.45.205.188:8080/recommend/consultrecsnorate?callback=foo&consultid=' + consultID + cmidList
        #url = 'http://10.115.100.77:8080/recommend/consultrecsnorate?callback=foo&consultid=' + consultID + cmidList
        # url = 'http://10.115.100.15:8081/recommend/consultrecsnorate?callback=foo&consultid=' + consultID + cmidList
        #print url
        self.makeCall( url )
            
if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
