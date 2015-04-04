from bs4 import BeautifulSoup
import time

fil = open('htmlWordList.txt','w')
fileNumber = 1
wordcount = {}
while True:
	fileName = str(fileNumber) + '.html'
	try:
		f = open(fileName,'r+')
		soup = BeautifulSoup(f)
		# kill all script and style elements
		for script in soup(["script", "style"]):
			script.extract()    # rip it out

		# get text
		text = soup.get_text()

		# break into lines and remove leading and trailing space on each
		lines = (line.strip() for line in text.splitlines())
		# break multi-headlines into a line each
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		# drop blank lines
		text = '\n'.join(chunk for chunk in chunks if chunk)
		tempFile = open('tempfile.txt','w')

		tempFile.write(text.encode('utf-8'))
		tempFile.close()
		tempFileagain = open('tempfile.txt','r+')

		for word in tempFileagain.read().split():
			word = word.translate(None, "!@#$%^&*()-=+_,.;{}[]<>?:\"`~")
			word = word.strip()
			word = word.lower()
			if word not in wordcount:
				wordcount[word] = 1
			else:
				wordcount[word] += 1
		tempFileagain.close()
		#print(text)
		fileNumber +=1
		if fileNumber == 10001:
			break
	except Exception, e:
		print e
		print fileNumber
		f.close()
		fileNumber +=1
		if fileNumber == 1001:
			break
		continue
for k,v in wordcount.items():
	fil.write(str(k))
	fil.write('\t')
	fil.write(str(v))
	fil.write('\n')
fil.close()
