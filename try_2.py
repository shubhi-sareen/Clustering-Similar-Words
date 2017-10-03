from sets import Set
from math import log
import re
import numpy as np
import matplotlib.pyplot as plt 

trainTopics = [] #lisdyt of list of topics, "None"  if no topic
trainTitle = []
trainBody = []

testTopics = [] #lisdyt of list of topics, "None"  if no topic
testTitle = []
testBody = []
termFrequency = list(dict())
with open("co_occur.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break


stopwords =[" ","be","by","at","up","this","was","some","if","have","been","will","and","all","which","last","would","over","on","not","no","it","of","or","in","from","about","were","a","an","the","has","had","for","with","other","its","as","to","between","is","are","also","before","after","they","that","their","there","not","than","but","he","she"]
uniqueWords = Set([])
for lines in trainBody:
	words = re.split('\s|(?<!\d)[,.]|[,.](?!\d)',lines)
	for word in words:
                word = word.lower()
		if "&" in word or '1' in word or '2' in word or '3' in word or '4' in word or '5' in word or '6' in word or '7' in word or '8' in word or '9' in word or '0' in word or '.' in word or word in stopwords or len(word) == 1:
			continue
		if "\'s" in word:
			uniqueWords.add(word[:-2])
			continue
		if ")" in word:
			uniqueWords.add(word[:-1])
			continue
		if "(" in word:
			uniqueWords.add(word[2:])
			continue
#		if word[len(word)-1] == 's':
#			if word[:-1] in uniqueWords:
#				continue
#			uniqueWords.add(word)#
		uniqueWords.add(word)
doc_count = {}
set_train_body = list(Set([]))
for body in trainBody:
	to_insert = {}
	s = Set([])
	for x in re.split('\s|(?<!\d)[,.]|[,.](?!\d)',body):
		x=x.lower()
		if "&" in x or '1' in x or '2' in x or '3' in x or '4' in x or '5' in x or '6' in x or '7' in x or '8' in x or '9' in x or '0' in x or '.' in x or x in stopwords or x not in uniqueWords:
			continue
		if "\'s" in x:
			s.add(x[:-2])
			continue
		if ")" in x:
			s.add(x[:-1])
			continue
		if "(" in x:
			s.add(x[2:])
			continue
		if x not in uniqueWords:
			continue
		if x not in to_insert:
			to_insert[x] = 1
		else:
			to_insert[x]+=1
		s.add(x)
	set_train_body.append(s)
	termFrequency.append(to_insert)

i = 1
uniqueWordsToIndex = {}
j = 0
for word in uniqueWords:
	uniqueWordsToIndex[word] = j
	j=j+1
arr = np.zeros((9772,9772))
k=0
for body in set_train_body:
	k=k+1
	for word_column in body:
		flag = 0
		for word_row in body:
			if word_column == word_row:
				if flag == 0:
					flag = 1
					continue
			arr[uniqueWordsToIndex[word_row],uniqueWordsToIndex[word_column]]+=1
	if k >set_train_body:
		print "error"
		break

uniqueWord=[]
for word in uniqueWords:
	uniqueWord.append(word)

la = np.linalg
U,s,Vh = la.svd(arr,full_matrices=False)



U[:,0] = (U[:,0]-np.mean(U[:,0]))/np.std(U[:,0])
U[:,1] = (U[:,1]-np.mean(U[:,1]))/np.std(U[:,1])
for i in range(len(uniqueWord)):
	try:
		plt.text(U[i,0],U[i,1],uniqueWord[i])
	except:
		print i
		continue
plt.xlim(np.min(U[:,0]),np.max(U[:,0]))
plt.ylim(np.min(U[:,1]),np.max(U[:,1]))
plt.show()

plt.scatter(U[:,0],U[:,1])
plt.xlim(np.min(U[:,0]),np.max(U[:,0]))
plt.ylim(np.min(U[:,1]),np.max(U[:,1]))
plt.show()

