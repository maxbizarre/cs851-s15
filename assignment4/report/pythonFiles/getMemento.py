import json
import os

w = open('mementoCount.txt', 'w+')
count = 1
while count < 10001:
	path = 'labs/' + str(count)
	
	if os.path.isfile(path):
		f = open(path, 'r+')
		if os.stat(path).st_size:
			try:
				data = json.loads(f.read())
				w.write(str(len(data['mementos']['list'])))
				w.write('\n')
				f.close()
			except KeyError:
				w.write(str(len(data['timemap_index'])))
				w.write('\n')
				f.close()
	count += 1
	print count
w.close()
