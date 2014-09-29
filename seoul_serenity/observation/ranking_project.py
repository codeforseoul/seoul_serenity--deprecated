import csv
import math

def read_csv(filename):
	with open(filename,'rb') as csvfile:
		reader=csv.reader(csvfile,delimiter=',')
		result=[]
		for row in reader:
			result.append(row)
	csvfile.close()
	return result			
		
def write_csv(result,output):
	with open(output,'wb') as csvfile:
		writer=csv.writer(csvfile,delimiter=',')
		for l in result:
			writer.writerow(l)
	csvfile.close()	

def createProjDic(data):
	projDic={}
	
	# create project list
	for d in data:
		if not d[col1] in projDic.keys():
			projDic[d[col1]]={}
			projDic[d[col1]][d[col2]]=[]
		elif not d[col2] in projDic[d[col1]].keys():
			projDic[d[col1]][d[col2]]=[]	
		projDic[d[col1]][d[col2]].append([int(d[col3]),d[col4]])
	
	return projDic

def createReviewerDic(data):
	reviewerDic={}
	
	for d in data:
		if not d[col2] in reviewerDic.keys():
			reviewerDic[d[col2]]={}
			reviewerDic[d[col2]][d[col1]]=[]
		elif not d[col1] in reviewerDic[d[col2]].keys():
			reviewerDic[d[col2]][d[col1]]=[]
		reviewerDic[d[col2]][d[col1]].append(int(d[col3]))
		
	return reviewerDic

def getReviewerStd(reviwerDic):
	reviewerStd={}
			
	for k1 in reviwerDic.keys():
		tmp_std=0
		for k2 in reviwerDic[k1].keys():
			tmp_std=tmp_std+math.sqrt(float(sum([x**2 for x in reviwerDic[k1][k2]]))/len(reviwerDic[k1][k2])-(float(sum(reviwerDic[k1][k2]))/len(reviwerDic[k1][k2]))**2)
		reviewerStd[k1]=tmp_std/len(reviwerDic[k1].keys())
		
	return reviewerStd
	
def sortby(item):
	return item[1]
	
def measure1(projDic,p,coeff):
	projScore={}
	
	# sort by date & weighted average &
	for k1 in projDic.keys():
		wavg=0
		for k2 in projDic[k1].keys():
			# sort
			projDic[k1][k2]=sorted(projDic[k1][k2],key=sortby,reverse=True)
			
			lenRate=len(projDic[k1][k2])
			coeff=coeff[0:min(lenRate,p)]
			
			# weighted average
			wavg=wavg+sum([x[0]*y for x,y in zip(projDic[k1][k2], coeff)])/sum(coeff)
			
		projScore[k1]=wavg/len(projDic[k1].keys())
	
	return projScore

def measure2_1(projDic,p,coeff,reviewerDic):
	reviewerStd=getReviewerStd(reviewerDic)
	projScore={}
		
	for k1 in projDic.keys():
		for k2 in projDic[k1].keys():
			# sort
			projDic[k1][k2]=sorted(projDic[k1][k2],key=sortby,reverse=True)
			
			lenRate=len(projDic[k1][k2])
			coeff=coeff[0:min(lenRate,p)]
			
			# deviation measure
			avg=sum([x[0] for x in projDic[k1][k2]])/sum(coeff)
			tmp=[(x[0]-avg)/max(0.001,reviewerStd[k2]) for x in projDic[k1][k2]]
			dev=sum([x*y for x,y in zip(tmp, coeff)])/sum(coeff)
			
		projScore[k1]=avg/len(projDic[k1].keys())
	
	return projScore

def measure2_2(projDic,p,coeff,reviewerDic):
	reviewerStd=getReviewerStd(reviewerDic)
	projScore={}
		
	for k1 in projDic.keys():
		for k2 in projDic[k1].keys():
			# sort
			projDic[k1][k2]=sorted(projDic[k1][k2],key=sortby,reverse=True)
			
			lenRate=len(projDic[k1][k2])
			coeff=coeff[0:min(lenRate,p)]
			
			# deviation measure
			avg=sum([x[0] for x in projDic[k1][k2]])/sum(coeff)
			tmp=[(x[0]-avg)/max(0.001,reviewerStd[k2]) if (x[0]-avg)/max(0.001,reviewerStd[k2])<0 else 0 for x in projDic[k1][k2]]
			dev=sum([x*y for x,y in zip(tmp, coeff)])/sum(coeff)
			
		projScore[k1]=avg/len(projDic[k1].keys())
	
	return projScore

# assumption
# -----------------
# data col 0: project ID
# data col 1: reviewer ID
# data col 2: rating
# data col 3: date
# -----------------
col1=0
col2=1
col3=2
col4=3

# set parameters
a=0.9
p=10
pp=[math.pow(0.9,x) for x in range(0,p)]

# load data
data=read_csv('D:/Personal/Python/sample_data.csv')

# create dictionaries for project, reviewer
projDic=createProjDic(data)
reviewerDic=createReviewerDic(data)

# measure 1
score1=measure1(projDic,p,pp)
print score1

# measure 2
score2=measure2_1(projDic,p,pp,reviewerDic)
print score2

