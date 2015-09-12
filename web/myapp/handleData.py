dataList = open("myapp/dataList.txt","r")
lines = dataList.readlines()
dataList.close()

myDict = {} #build a dict from key word to food id
for line in lines:
	line = line[:-1].split(",")
	myDict[line[0]] = line[1:]

func = ["*",] #build a list from food id to food name
file = open("myapp/list.txt","r")
mylist = file.readlines()
file.flush()
for item in mylist:
	func.append(item.split(",")[1][:-1])
file.close()

size = 279