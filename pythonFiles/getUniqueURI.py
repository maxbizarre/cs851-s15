#CS751 Spring 2015 Offered by Dr. Michael Nelson - Assignment 1
#Filename: getUniqueURI.py
#Author: Khaja Masroor Ahmed
#UIN: 00999044
#CS Email: kahmed@cs.odu.edu

import json
import sets

f = open('status.txt','r+')
w = open('unique.txt','w')
uniqueURLs = sets.Set()
count = 1
for line in f:
	data = json.loads(line)
	for urlData in data['tweetURLData']:
		uniqueURLs.add(urlData['finalURL'])
		count = count + 1
w.write('Unique: ' + (str)(len(uniqueURLs)) + '\n')
w.write('Duplicates: ' + (str)(count - len(uniqueURLs)) + '\n')
w.write('Total: ' + (str)(count) + '\n')
f.close()
w.close()
