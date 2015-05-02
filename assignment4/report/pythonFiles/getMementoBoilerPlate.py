import json
import os
from boilerpipe.extract import Extractor

count = 1
while count < 10001:
	if count == 182 or count == 714 or count == 1106 or count == 1200 or count == 1417 or count == 2077 or count == 2168 or count == 2235 or count == 2338 or count == 2604 or count == 5209 or count == 5986 or count == 6591 or count == 6969 or count == 7861 or count == 8145 or count == 8827 or count == 9093 or count == 9548 or count == 9613:
		print count
		path = 'labs/' + str(count)
	
		if os.path.isfile(path):
			f = open(path, 'r+')
			if os.stat(path).st_size:
				data = json.loads(f.read())
				if not os.path.exists(str(count)):
					os.makedirs(str(count))
				
				filecounter = 1
				link = str(count) + '_datetime.txt'
				g = open(link, 'w')
				for url in data['mementos']['list']:
					extractor = Extractor(extractor='DefaultExtractor', url=url['uri'])
					extracted_text = extractor.getText()
					g.write(str(url['datetime']))
					g.write('\n')
				g.close()
				filecounter += 1					
			f.close()
	count += 1
