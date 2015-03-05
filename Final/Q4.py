import urllib
import httplib
import json
import datetime, time
import numpy as np
import pylab as pl
from numpy import polyfit
import math

# getting max number of retweets
length=0
with open('tweets.txt','r') as ifile:
	for line in ifile.readlines():
		tweet = json.loads(line)
		if(!tweet['tweet']['retweeted']):
			length = max(length,tweet['tweet']['retweet_count'])

ifile.close()
 

		
# updating retweets count array
array=[0]*(length+1)
xaxis = [0]*(length+1)
npx = np.zeros(length+1)
with open('tweets.txt','r') as infile:
	for line in infile.readlines():
		tweet = json.loads(line)
		if(!tweet['tweet']['retweeted']):
			i = tweet['tweet']['retweet_count']
			array[i] = array[i]+1
			xaxis[i] = i
			npx[i] = i

infile.close()

print array 
# plotting the linear graph
pl.plot(xaxis,array)
p = np.polyfit(xaxis,array,1)
pl.plot(npx,p[0]*npx + p[1])
pl.xlabel("k")
pl.ylabel("Number of tweets retweeted k times")
pl.show()


#log-log graph

array[0] = math.log10(array[0])
for i in range(1,length+1):
	xaxis[i] = math.log10(i)
	npx[i] = math.log10(i)
	if array[i] > 0:
		array[i] = math.log10(array[i])
	
print array 
pl.plot(xaxis,array)
p = np.polyfit(xaxis,array,1)
pl.plot(npx,p[0]*npx + p[1])
pl.xlabel("log(k)")
pl.ylabel("log(Number of tweets retweeted k times)")
pl.show()

        	
