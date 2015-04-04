import json
from boilerpipe.extract import Extractor

f = open('status.txt', 'r+')
for line in f:
	data = json.loads(line)
	try:
		if data['index'] == 10001:
			print 'Program Executed'
			break
		finalURL=data['tweetURLData'][0]['finalURL']
		extractor = Extractor(extractor='DefaultExtractor', url=finalURL)
		extracted_text = extractor.getText()
		link = str(data['index']) + '.txt'
		g = open(link, 'w')
		g.write(extracted_text.encode('utf-8'))
		g.close()
	except:
		print data['index']
		continue
