
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

def buildArray():
    basepath = os.path.dirname(__file__)
    fileTarget = os.path.join(basepath, "QueriesNotEnc.txt")
    try:
        array = [ line.strip() for line in file(fileTarget) ]
    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        sys.exit()
    
    return array

def writeErrorInfo(myInfo):
    
    basepath = os.path.dirname(__file__)
    fileTarget = os.path.join(basepath, "testinfo.txt")

    try:
        logfile = open(fileTarget, "a")
        print >> logfile, myInfo
        logfile.close()
    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        sys.exit()

class Transaction(object):
    def __init__(self):
        self.custom_timers = {}
        self.word_list = buildArray( )
        self.word_list_length = len(self.word_list)

    
    def makeCall( self, url ):
        start_timer = time.time()
        r = requests.get(url)
    
        #content = r.text
        #print content
    
        latency = time.time() - start_timer
    
        self.custom_timers['trie_service'] = latency
    
        if latency > 5:
            writeErrorInfo('latency value of %f with %s' %(latency, url) )
        if r.status_code != 200:
            writeErrorInfo('status code with %s is %s' %(r.status_code, url) )
    
        assert (r.status_code == 200), 'Bad HTTP Response'
        assert ('foo' in r.text), 'No foo'
    
    def run(self):
        #get a random word from the word_list and call to typeahead
        whichPhrase = random.randrange(0,self.word_list_length)
        phrase = self.word_list[whichPhrase]
        word = phrase.split(" ")[0]
        #print 'word is %s' % word
        item = ""
        url = ""
        #loop through the chars in the word skipping the first
        for char in word:
            item = item + char
            if len(item) > 1:
                url = 'http://10.45.205.80:8080/typeahead/trie/?entity=org&value=' + item + '&callback=foo'
                #url = 'http://10.20.41.208:8080/typeahead/trie/?entity=org&value=' + item + '&callback=foo'
                self.makeCall( url )
            
if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
