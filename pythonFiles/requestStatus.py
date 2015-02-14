#CS751 Spring 2015 Offered by Dr. Michael Nelson - Assignment 1
#Filename: requestStatus.py
#Author: Khaja Masroor Ahmed
#UIN: 00999044
#CS Email: kahmed@cs.odu.edu

import requests 
import json
import string

f = open('output.txt', 'r+')
w = open('status.txt','w')
err = open('error.txt','w')
count = 1
for line in f:
	data = json.loads(line)
	i = 0
	try:
		tweetData = {}
		tweetData['index'] = count
		tweetData['tweetId'] = data['tweetId']
		tweetData['createdDate'] = data['createdAt']
		tweetURLData = []
		for url in data['url']:
			
			r = requests.head(data['url'][i], allow_redirects=True, timeout = 15)
			j = 0
			
			URLData = {}
			
			URLData['finalURL'] = r.url
			statusCode = []
			statusCode.append(r.status_code)
			for response in r.history:
				statusCode.append(response.status_code)
			URLData['statusCode'] = statusCode
			URLData['tweetURL'] = data['url'][i]
			tweetURLData.append(URLData)
			
			i = i + 1
		tweetData['tweetURLData'] = tweetURLData

		tweetData = json.dumps(tweetData)
		print count	
		w.write(tweetData + "\n")
	except:
		err.write(str(count) + '\n')
		continue
	count = count + 1
f.close()
w.close()
err.close()
