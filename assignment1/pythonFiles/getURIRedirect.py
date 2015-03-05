#CS751 Spring 2015 Offered by Dr. Michael Nelson - Assignment 1
#Filename: getURIRedirect.py
#Author: Khaja Masroor Ahmed
#UIN: 00999044
#CS Email: kahmed@cs.odu.edu

import json

f = open('status.txt','r+')
w = open('uriRedirect.txt','w')
w2 = open('uriRedirectCount.txt','w')
uriRedirect = {}
for line in f:
	data = json.loads(line)
	count = 0
	for tweetData in data['tweetURLData']:
		for status in tweetData['statusCode']:
			if(str(status).startswith('3')):
				count = count + 1
		w.write(str(count) + '\t' + tweetData['finalURL'] + '\n')
		if count in uriRedirect:
			uriRedirect[count] = uriRedirect[count] + 1
		else:
			uriRedirect[count] = 1
w2.write(str(uriRedirect) + '\n')
w.close()
w2.close()
