from nltk.util import ngrams
import os

MAX_NGRAMS=1

def jaccardDistance(list1, list2):
	union = set(list1).union(list2)
	intersect = set(list1).intersection(list2)
	if len(union) == 0:
		return 0
	dist = (len(union) - len(intersect)) * 1.0 / len(union)
	return dist

def getNGrams(fileName):
	f = open(fileName, 'r+')
	unigramList=[]
	notEntered = True
	#print fileName
	for line in f:
		notEntered = False
		unigram = ngrams(line.split(), MAX_NGRAMS)
		for grams in unigram:
			unigramList.append(grams)
		#print len(unigramList)
		#print unigramList
		if len(unigramList) == 0:
			print fileName
			return unigramList,True
	f.close()
	if notEntered:
		return unigramList, True
	return unigramList, False

def fileExists(fileName):
	return os.path.isfile(fileName)
count = 1

while count < 10001:
	if os.path.exists(str(count)):
		print str(count)
		fileCounter = 1
		fileName1 = str(count) + '/' + str(fileCounter) + '.txt'
		if fileExists(fileName1):
			unigramListBaseline=[]
			shouldExit = False
			unigramListBaseline, shouldExit = getNGrams(fileName1)
			#print shouldExit
			if shouldExit:
				fileCounter += 1
				fileName1 = str(count) + '/' + str(fileCounter) + '.txt'
				unigramListBaseline=[]
				shouldExit = False
				unigramListBaseline, shouldExit = getNGrams(fileName1)
				print 'exit1'
			#print unigramListBaseline
			uni = open(str(count) + '_jaccard.txt','w')
			while fileCounter < 1000:
				fileCounter += 1
				fileName2 = str(count) + '/' + str(fileCounter) + '.txt'
				if fileExists(fileName2):
					unigramListCurrent=[]
					shouldExit = False
					unigramListCurrent, shouldExit = getNGrams(fileName2)
					#print shouldExit
					if shouldExit:
						print 'exit2'
						#count += 1
						uni.write(str(1.0))
						uni.write('\n')
						continue
					#print str(len(unigramListBaseline)) + '\t' + str(len(unigramListCurrent))
				
					uni.write(str(jaccardDistance(unigramListBaseline,unigramListCurrent)))
					uni.write('\n')

			uni.close()
	count += 1

print 'Program Executed'
