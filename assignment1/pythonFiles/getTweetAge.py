import json
import datetime

f = open('carbonData.txt','r+')
w = open('age.txt','w')
count = 0
for line in f:
	data = json.loads(line)
	if data['oldestDate'] != '':
		count = count + 1
		oldestDate = datetime.datetime.strptime(data['oldestDate'], '%Y-%m-%dT%H:%M:%S')
		createdDate = datetime.datetime.strptime(data['createdDate'], "%a %b %d %H:%M:%S +0000 %Y")
		age = abs((oldestDate.date() - createdDate.date()).days) 
		w.write(str(age) +'\n')
print('Execution Complete')

