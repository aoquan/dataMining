### author: aoquan
### written by python

import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
import pylab as pl
import scipy.stats as stats

season = ['spring','summer','autumn','winter']
seasonCount = [0,0,0,0]
riverSize = ['small','medium','large']
riverSizeCount = [0,0,0]
riverSpeed = ['low','medium','high']
riverSpeedCount = [0,0,0]

item = ['season','riverSize','riverSpeed','mxPH','mnO2','Cl','NO3','NH4','oPO4','PO4','Chla','a1','a2','a3','a4','a5','a6','a7']
data = [[] for i in range(18)]


def getFrequency(array1,array2):
	length =  len(array1)
	for i in range(0,length):
		print array1[i],'	',array2[i]

def plotHistogram(array,picName):
	xData = np.arange(len(array))
	fig = plt.figure()
	figure = plt.gcf() # get current figure
	#figure.set_size_inches(19, 20)
	ax1 = fig.add_subplot(111)
	ax1.plot(xData, array,'r',label="frequency")
	# ax1.plot(xData, array,'b.')
	ax1.set_ylabel('frequency')
	ax1.set_xlabel('start_time')
	plt.savefig(picName)

def hist(array):
	length = len(array)
	maxValue = max(array)
	minValue = min(array)
	dis = maxValue - minValue
	bins = 20
	interval = dis/bins
	result = [0]*bins
	for i in range(0,length):
		pos = int((array[i]-minValue)/(dis/bins))
		if (pos == bins):
			pos = bins - 1
		result[pos] += 1
	return result



m = 0
fpIn = open('Analysis.txt','r')
lines = fpIn.readlines()
for line in lines:
	para = line.split()
	### nominal attribute
	for i in range(0,4):
		if(para[0]== season[i]):
			seasonCount[i] += 1
	for i in range(0,3):
		if (para[1] == riverSize[i]):
			riverSizeCount[i] += 1
	for i in range(0,3):
		if (para[2] == riverSpeed[i]):
			riverSpeedCount[i] += 1
	for n in range(0,18):
		data[n].append(para[n])

	m += 1


# getFrequency(season,seasonCount)
# getFrequency(riverSize,riverSizeCount)
# getFrequency(riverSpeed,riverSpeedCount)

for i in range(3,18):
	tmp = data[i]
	j = 0
	while('XXXXXXX' in tmp):
		tmp.remove('XXXXXXX')
		j += 1
	tmp = [float(k) for k in tmp]
	tmp.sort()
	length = len(tmp)
	if (length %2 ==0 ):
		mid = (tmp[length/2-1] + tmp [length/2])*0.5
	else:
		mid = tmp[length/2-1]
	print item[i],'    ',str(max(tmp)),'    ',str(min(tmp)),'    ',str(sum(tmp)/length),'    ',str(mid),'    ',str(j)

	# arrayHist = hist(tmp)
	# print arrayHist
	# plotHistogram(arrayHist,str(i)+'.svg')

	## histgram
	bins = 20
	pl.figure()
	pl.hist(tmp,bins)
	pl.savefig(str(i)+'.svg')
	pl.close()
	#pl.show()

	## Q-Q plot
	pl.figure()
	stats.probplot(tmp, dist="norm", plot=plt)
	plt.title("Normal Q-Q plot")
	plt.savefig(str(i)+'qq.svg')
	plt.close()
	#plt.show()

	## box plot
	# Create a figure instance
	fig = plt.figure(1, figsize=(9, 6))
	# Create an axes instance
	ax = fig.add_subplot(111)
	# Create the boxplot
	bp = ax.boxplot(tmp)
	# Save the figure
	fig.savefig(str(i)+'box.svg', bbox_inches='tight')
	plt.close()








