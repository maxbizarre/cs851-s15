import os
import datetime
import json

TIME_MAP_URL = "http://labs.mementoweb.org/timemap/json/"

f = open('status.txt', 'r+')
print datetime.datetime.now()
for line in f:
	data = json.loads(line)
	try:
		if data['index'] == 10001:
			print 'Program Executed'
			break
		finalURL=data['tweetURLData'][0]['finalURL']
		print '-----------------------------------------------------------------------------------------------'
		os.system("wget --output-document=" + str(data['index']) + " " + TIME_MAP_URL + finalURL)
	except:
		continue
print datetime.datetime.now()
