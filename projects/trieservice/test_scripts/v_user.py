
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

class Transaction(object):
    def __init__(self):
        self.custom_timers = {}
        self.word_list = buildArray( )
        self.word_list_length = len(self.word_list)
    
    def run(self):
        #get a random word from the word_list and call to typeahead
        whichword = random.randrange(0,self.word_list_length)
        word = self.word_list[whichword]
        #print 'word is %s' % word
        item = ""
        for char in word:
            item = item + char
            url = 'http://10.45.205.204:8080/typeahead/trie/?entity=org&value=%s&callback=foo' % item
            #print url
            start_timer = time.time()
            r = requests.get('http://10.45.205.204:8080/typeahead/trie/?entity=org&value=' + char + '&callback=foo')
        
        
            #content = r.text
            #print content
        
            latency = time.time() - start_timer
        
            self.custom_timers['trie_service'] = latency
        
            if latency > 1:
                print url    
            assert (r.status_code == 200), 'Bad HTTP Response'
            assert ('foo' in r.text), 'No foo'


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
