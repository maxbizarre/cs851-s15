from twarc import Twarc
import json

CONSUMER_KEY = 'CfHUyBhlMaLv5Mn8r2IziXpLs'
CONSUMER_SECRET = 'PqqtbhbyNb5mcJ2dHkSIT2wupOMuEqfSINGYvV8KDIOPuqgDkN'
ACCESS_TOKEN = '29202483-qK6twPLeurVc8Ls8zBxdFtaFGyzm76LUBbtXOMMk1'
ACCESS_TOKEN_SECRET = 'aOIFdI1TVJjsIPWNO1rAFx2IECzVSCPY4kOnEKBA0pCdA'

w = open('tweetDay5.json', 'w')

t = Twarc(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
count = 1
for tweet in t.search("google fi"):
	w.write(json.dumps(tweet))
	w.write('\n')
	print count
	count += 1
	if count >1000:
		break

