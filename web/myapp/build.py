#coding:utf8
import HTMLParser,re
i = 0
file = 0
myDict = {}
flag = 0
div = 0
class myParser(HTMLParser.HTMLParser):
	def handle_starttag(self, tag, attrs):
		global flag, div
		if (flag == 1):
			div += 1
		elif (tag=='div'):
			for item in attrs:
				if ((item[0] == 'id') and (item[1] == 'bodyContent')):
					flag = 1
					div = 1
	
	def handle_endtag(self, tag):
		global flag, div
		if (flag == 0):	
			div -= 1
			if (div == 0):
				flag = 0
				
	def handle_data(self,data):
		global i,myDict,flag
		if flag == 0:
			return
		dataList = data.split()
		for item in dataList:
			if item.isalpha() == True:
				item = item.lower()
				#myDict[item].append(i)
				
				#if item == "rice"and i == 278:
				#	print data
				if not (item in myDict):
					myDict[item] = [i]
				elif (myDict[item][-1] != i):
					myDict[item].append(i)
				
parser = myParser()

pattern = re.compile(r'<div id="bodyContent"')
while i < 278:
	i += 1
	print str(i) + ".html"	
	file = open("templates/" + str(i) + ".html","r")
	if not file:
		continue
	content = file.read()
	match = pattern.search(content)
	print match.pos
	content = content[match.pos:]
	parser.feed(content)			
	file.close()

file = open("dataList.txt","w")
for item in myDict.keys():
	file.write(item)
	for num in myDict[item]:
		file.write("," + str(num))
	file.write("\n")
file.close()