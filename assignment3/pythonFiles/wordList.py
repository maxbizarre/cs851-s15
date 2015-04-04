import wordcount
import re
import sys

fil = open('wordList.txt','w')
fileNumber = 1
wordcount = {}
while True:
	fileName = str(fileNumber) + '.txt'
	try:
		f = open(fileName,'r+')
		
		for word in f.read().split():
			word = word.translate(None, "!@#$%^&*()-=+_,.;{}[]<>?:\"`~")
			word = word.strip()
			word = word.lower()
			if word not in wordcount:
				wordcount[word] = 1
			else:
				wordcount[word] += 1
		f.close()
		fileNumber +=1
		if fileNumber == 10001:
			break
	except Exception, e:
		print e
		f.close()
		fileNumber +=1
		continue
for sortedValue in sorted(wordcount.values()):
	fil.write(str(sortedValue))
	fil.write('\t')
	fil.write(wordcount[sortedValue])
	fil.write('\n')
fil.close()
