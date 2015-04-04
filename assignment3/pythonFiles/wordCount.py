import wordcount
import re
import sys

fil = open('wordCount.txt','w')
fileNumber = 1
while True:
	count = 0
	fileName = str(fileNumber) + '.txt'
	try:	
		f = open(fileName,'r+')
		fil.write(fileName)
		wordcount = {}
		for word in f.read().split():
			newword = word
			word = word.translate(None, "!@#$%^&*()-=+_,.;{}[]<>?:\"`~")
			word = word.strip()
			word = word.lower()
			if word not in wordcount:
				wordcount[word] = 1
			else:
				wordcount[word] += 1
			count +=1
		fil.write('\t')
		fil.write(str(count))
		fil.write('\n')
		f.close()
		print fileNumber
		fileNumber +=1
		if fileNumber == 10001:
			sys.exit()
	except Exception, e:
		print e
		f.close()
		fileNumber +=1
		continue
fil.close()
