#CS751 Spring 2015 Offered by Dr. Michael Nelson - Assignment 1
#Filename: getStatusCodeFrequency.py
#Author: Khaja Masroor Ahmed
#UIN: 00999044
#CS Email: kahmed@cs.odu.edu

import json
import string

f = open('status.txt', 'r+')
w = open('statusCode.txt', 'w')
statusCode = {}
for line in f:
	data = json.loads(line)
	if data['index'] == 10000:
		print 'Program Executed'
		break
	for tweetData in data['tweetURLData']:
		for status in tweetData['statusCode']:
			w.write(str(status) + '\n')
			if status in statusCode:
				statusCode[status] = statusCode[status] + 1
			else:
				statusCode[status] = 1
