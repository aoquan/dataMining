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

# def plotHistogram(array,picName):
# 	xData = np.arange(len(array))
# 	fig = plt.figure()
# 	figure = plt.gcf() # get current figure
# 	#figure.set_size_inches(19, 20)
# 	ax1 = fig.add_subplot(111)
# 	ax1.plot(xData, array,'r',label="frequency")
# 	# ax1.plot(xData, array,'b.')
# 	ax1.set_ylabel('frequency')
# 	ax1.set_xlabel('start_time')
# 	plt.savefig(picName)

# def hist(array):
# 	length = len(array)
# 	maxValue = max(array)
# 	minValue = min(array)
# 	dis = maxValue - minValue
# 	bins = 20
# 	interval = dis/bins
# 	result = [0]*bins
# 	for i in range(0,length):
# 		pos = int((array[i]-minValue)/(dis/bins))
# 		if (pos == bins):
# 			pos = bins - 1
# 		result[pos] += 1
# 	return result

# def NormalData(data):



def FillMissValueByFrequency(array):
	maxCount = 0
	value = 0
	for data in array:
		if 'X' not in data:
			tmpCount = array.count(data)
			if (tmpCount > maxCount):
				maxCount =  tmpCount
				value = data 
	for data in array:
		if 'X' in data:
			data = value
	print array

	return array

# def FillMissValueBySimilar(data):
# 	for line in data:




def HistPlot(tmp,bins,name):
	pl.figure()
	pl.hist(tmp,bins)
	pl.savefig(name+'hist.svg')
	pl.close()

def QQPlot(tmp,name):
	pl.figure()
	stats.probplot(tmp, dist="norm", plot=plt)
	plt.title("Normal Q-Q plot")
	plt.savefig(name+'qq.svg')
	plt.close()

def BoxPlot(tmp,name):
	fig = plt.figure(1, figsize=(9, 6))
	ax = fig.add_subplot(111)
	bp = ax.boxplot(tmp)
	fig.savefig(name+'box.svg', bbox_inches='tight')
	plt.close()

def ConditionBoxPlt(condition,countData,name,m):
	lenCon = len(condition)
	conTmp = [[] for i in range(lenCon)]
	for i in range(11,18):
		for j in range(0,countData):
			index = condition.index(data[m][j])
			if ('X' not in data[i][j]):
				conTmp[index].append(data[i][j])

		fig = plt.figure()
		for j in range(1,lenCon+1):
			ax = fig.add_subplot(1,lenCon,j)
			conTmp[j-1] = [float(k) for k in conTmp[j-1]]
			bp = ax.boxplot(conTmp[j-1])
			
		fig.savefig(name+'_'+item[i]+'Conbox.svg', bbox_inches='tight')
		plt.close()


def DataVisual(nameAppend):
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

		
		print item[i],'    ',str(max(tmp)),'    ',str(min(tmp)),'    ',str(sum(tmp)/length),'    ',str(mid),'    ',str(np.percentile(tmp,25)),'    ',str(np.percentile(tmp,75)),'    ',str(j)

		HistPlot(tmp,20,str(i)+nameAppend)
		QQPlot(tmp,str(i)+nameAppend)
		BoxPlot(tmp,str(i)+nameAppend)

#def CovRaltion():




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




# getFrequency(season,seasonCount)
# getFrequency(riverSize,riverSizeCount)
# getFrequency(riverSpeed,riverSpeedCount)


# dataCp = data
# DataVisual('Ori')


for  i in range(3,18):
	data[i] = FillMissValueByFrequency(data[i])

fp = open('after.txt','wt')
for j in range(0,200):
	for i in range(0,18):
		fp.write(data[i][j]+"    ")
	fp.write('\n')
fp.close()



# DataVisual(data,'Fre')


# ConditionBoxPlt(season,len(data[0]),'season',0)
# ConditionBoxPlt(riverSize,len(data[0]),'riverSize',1)
# ConditionBoxPlt(riverSpeed,len(data[0]),'riverSpeed',2)




# dataDirty = [[] for i in range(18-3)]
# dataClean = [[] for i in range(18-3)]
# for i in range(0,len(data[0])):
# 	flag =0
# 	for j in range(3,18):
# 		if('X' in data[j][i]):
# 			flag =1
# 			dataDirty[j-3].append(data[j][i])
# 			break
# 	if (flag == 1):
# 		continue
# 	for j in range(3,18):
# 		dataClean[j-3].append(data[j][i])

# for j in range(3-3,18-3):
# 	dataClean[j] = [float(k) for k in dataClean[j]]






# npMatrix = np.array(dataClean)

# cov = np.cov(npMatrix)
# peakIndex = np.argmax(cov)
# print cov
# print peakIndex

############################################
# dataCleanBk = dataClean
# for j in range(3-3,18-3):
# 	maxj = max(dataClean[j])
# 	minj=  min(dataClean[j])
# 	for  i in range(0,len(dataClean[0])):
# 		dataClean[j][i] = (dataClean[j][i]-minj)/(maxj-minj)

# 	for i in range(0,len(dataDirty[0])):
# 		print i,j
# 		if ('X' not in dataDirty[j][i]):
# 			dataDirty[j][i] = (dataDirty[j][i]-minj)/(maxj-minj)

# pos = 0
# maxV = 0 
# maxP =0
# # print dataDirty[j]
# for i in range(0,len(dataClean[0])):
# 	maxV = 0 
# 	for j in range(3,18):
# 		if ('X' not in dataDirty[j][0]):
# 			maxV += dataClean[j][i]*dataDirty[j][0]

# 	if (maxP < maxV):
# 		maxP = maxV
# 		pos = i

# print maxP,i

# print dataClean





