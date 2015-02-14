from checkForModules import checkForModules
import json
from ordereddict import OrderedDict
import urlparse
import re

from getBitly import getBitlyCreationDate
from getArchives import getArchivesCreationDate
from getGoogle import getGoogleCreationDate
from getBacklinks import *
from getLowest import getLowest

from getLastModified import getLastModifiedDate
from getTopsyScrapper import getTopsyCreationDate
from htmlMessages import *
from pprint import pprint

from threading import Thread
import Queue
import datetime

import os,sys, traceback




def cd(url, backlinksFlag = False):

    #print 'Getting Creation dates for: ' + url


    #scheme missing?
    parsedUrl = urlparse.urlparse(url)
    if( len(parsedUrl.scheme)<1 ):
        url = 'http://'+url
    
    
    threads = []
    outputArray =['','','','','','']
    now0 = datetime.datetime.now()
    
   
    lastmodifiedThread = Thread(target=getLastModifiedDate, args=(url, outputArray, 0))
    bitlyThread = Thread(target=getBitlyCreationDate, args=(url, outputArray, 1))
    googleThread = Thread(target=getGoogleCreationDate, args=(url, outputArray, 2))
    archivesThread = Thread(target=getArchivesCreationDate, args=(url, outputArray, 3))
    
    if( backlinksFlag ):
        backlinkThread = Thread(target=getBacklinksFirstAppearanceDates, args=(url, outputArray, 4))

    topsyThread = Thread(target=getTopsyCreationDate, args=(url, outputArray, 5))
    

    # Add threads to thread list
    threads.append(lastmodifiedThread)
    threads.append(bitlyThread)
    threads.append(googleThread)	
    threads.append(archivesThread)

    if( backlinksFlag ):
        threads.append(backlinkThread)

    threads.append(topsyThread)	

    
    # Start new Threads
    lastmodifiedThread.start()
    bitlyThread.start()
    googleThread.start()
    archivesThread.start()

    if( backlinksFlag ):
        backlinkThread.start()

    topsyThread.start()

    
    # Wait for all threads to complete
    for t in threads:
        t.join()
        
    # For threads
    lastmodified = outputArray[0]
    bitly = outputArray[1] 
    google = outputArray[2] 
    archives = outputArray[3] 
    
    if( backlinksFlag ):
        backlink = outputArray[4]
    else:
        backlink = ''

    topsy = outputArray[5]  
    
    #note that archives["Earliest"] = archives[0][1]
    try:
        lowest = getLowest([lastmodified, bitly, google, archives[0][1], backlink, topsy]) #for thread
    except:
       print sys.exc_type, sys.exc_value , sys.exc_traceback

    
    
    result = []
    
    result.append(("URI", url))
    result.append(("Estimated Creation Date", lowest))
    result.append(("Last Modified", lastmodified))
    result.append(("Bitly.com", bitly))
    result.append(("Topsy.com", topsy))
    result.append(("Backlinks", backlink))
    result.append(("Google.com", google))
    result.append(("Archives", archives))
    values = OrderedDict(result)
    r = json.dumps(values, sort_keys=False, indent=2, separators=(',', ': '))
    
    now1 = datetime.datetime.now() - now0

    print 'runtime in seconds:  ' +  str(now1.seconds) + '\n' + r + '\n'

    return lowest
    
f = open('status.txt', 'r+')
w = open('carbonDate.txt', 'w')

for line in f:
	data = json.loads(line)
	
	for tweetData in data['tweetURLData']:
		print data['index']
		print datetime.datetime.now()
		carbonDate = {}
		carbonDate['oldestDate'] = cd(tweetData['finalURL'])
		carbonDate['createdDate'] = data['createdDate']
		carbonDate['tweetId'] = data['tweetId']
		carbonDate = json.dumps(carbonDate)
		w.write(carbonDate + "\n")
		print carbonDate
