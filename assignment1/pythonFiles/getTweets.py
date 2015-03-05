#CS751 Spring 2015 Offered by Dr. Michael Nelson - Assignment 1
#Filename: getTweets.py
#Author: Khaja Masroor Ahmed
#UIN: 00999044
#CS Email: kahmed@cs.odu.edu

import tweepy
import json
import time
import datetime

consumer_key = "iuKUndPfIF5aWnNl0Ayq9Ztgt"
consumer_secret = "QuNsF4gL2LssmbcdtKpyLZGiQctz98T4hXWcAKrBYGh72ZTFC8"

access_token = "549294315-P89swbZzgiP2n9bq6fW2T2jm5etru6Wr6TN08Lg3"
access_token_secret = "NMzDaS5doFtHxXxebE68AunmRHTsFfLxwAkk3LsDN75JH"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
f = open('output.txt','w')
        
tweetCount = 1
print('Started execution')
cursor = tweepy.Cursor(api.search, q ='http:', since_id = 2014).items()
while True:
	try:
		tweet = cursor.next()
		for tweet in cursor:
			tweetData = {}
			tweetData['tweetId'] = tweet.id
			tweetData['createdAt'] = tweet._json['created_at']
			tweetData['userId'] = tweet.user._json['id']
			tweetData['tweetCount'] = tweetCount
			tweetData['text'] = tweet.text
			urlData = []

			for url in tweet._json['entities']['urls']:
				urlData.append(url['url'])
			tweetData['url'] = urlData
			tweetData = json.dumps(tweetData)

			if tweetCount == 11999:
				print('Complete')
				print(datetime.datetime.now())
				f.close()
				break
			f.write(tweetData + "\n")
			tweetCount = tweetCount + 1
	except tweepy.TweepError as e:
		print(e)
		time.sleep(900)
		continue
	except StopIteration:
		break
print('Program Executed!')
