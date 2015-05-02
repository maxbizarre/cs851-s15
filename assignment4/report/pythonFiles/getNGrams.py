from nltk.util import ngrams
import os

MAX_NGRAMS=3

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
	bigramList=[]
	trigramList=[]
	
	for line in f:
		unigram = ngrams(line.split(), MAX_NGRAMS-2)
		bigram = ngrams(line.split(), MAX_NGRAMS-1)
		trigram = ngrams(line.split(), MAX_NGRAMS)
		for grams in unigram:
			unigramList.append(grams)
		#print len(unigramList)
		#print unigramList
		if len(unigramList) == 0:
			print fileName
			return unigramList,bigramList,trigramList,True
		for grams in bigram:
			bigramList.append(grams)
		for grams in trigram:
			trigramList.append(grams)
	f.close()
	return unigramList, bigramList, trigramList, False

def fileExists(fileName):
	return os.path.isfile(fileName)
count = 1
uni = open('unigramOutput.txt','w')
bi = open('bigramOutput.txt','w')
tri = open('trigramOutput.txt','w')
while count < 10001:
	fileName1 = 'a3/' + str(count) + '.txt'
	fileName2 = 'a4/' + str(count) + '.txt'
	if fileExists(fileName1) and fileExists(fileName2):
		unigramListA3=[]
		bigramListA3=[]
		trigramListA3=[]
		shouldExit = False
		unigramListA3, bigramListA3, trigramListA3, shouldExit = getNGrams(fileName1)
		
		if shouldExit:
			print 'exit'
			count += 1
			continue

		unigramListA4=[]
		bigramListA4=[]
		trigramListA4=[]
		unigramListA4, bigramListA4, trigramListA4, shouldExit = getNGrams(fileName2)

		if shouldExit:
			print 'exit2'
			count += 1
			continue
		#print str(jaccardDistance(unigramListA3,unigramListA4))
		uni.write(str(jaccardDistance(unigramListA3,unigramListA4)))
		uni.write('\n')
		bi.write(str(jaccardDistance(bigramListA3,bigramListA4)))
		bi.write('\n')
		tri.write(str(jaccardDistance(trigramListA3,trigramListA4)))
		tri.write('\n')
	count += 1
uni.close()
bi.close()
tri.close()
print 'Program Executed'
