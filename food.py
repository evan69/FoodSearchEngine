import urllib2,HTMLParser,re
start = 1 #whether the parser enters the table(from 0 to 2)
intr = 0 #whether the parser enters a row
intd = 0 #whether the parser enters the first coloum
L = []
cnt = 0 #total number of food
flag = 0
class myParser(HTMLParser.HTMLParser):
	def handle_starttag(self,tag,attrs):
		global start,intr,intd,L,cnt,flag
		if(start == 1 and tag == "table" and attrs[0][0] == "class" and attrs[0][1][0:9] == "wikitable"):
			start = 2 #enter the table which will be proceeded
			return
		if(start < 2):
			return #data has been proceeded , do nothing
		if(tag == "tr" and intr == 0):
			intr = 1 #enter a row in a table
		if(intr == 0):
			return #first coloum has been proceeded
		if(tag == "td" and intd == 0 and intr == 1):
			intd = 1 #enter the first coloum in a row
		if(tag == "a" and attrs[0][0] == "href" and intd == 1):
			intr = 0
			if(attrs[0][1][:6] == "/wiki/"):	#valid coloum
				cnt = cnt + 1
				flag = 1
				data = attrs[0][1]
				#string = urllib2.urlopen("https://en.wikipedia.org" + data).read()
				data = data.split("/")[2]
				#tmp = open(str(cnt) + ".html","w")			
				#tmp.write(string)
				#tmp.flush()
				#tmp.close()			
	def handle_endtag(self,tag):
		global intr,intd,start
		if(tag == "table"):
			start = 0 #leave the table
		if(tag == "td"):
			intd = 0 #leave a coloum in the table
			intr = 0 #leave a row in the table
	def handle_data(self,data):
		global flag,cnt
		if flag == 1:
			print cnt,data
			L.append(data)
			flag = 0
parser = myParser()
req = urllib2.Request("https://en.wikipedia.org/wiki/List_of_rice_dishes")
response = urllib2.urlopen(req)
parser.feed(response.read())
print "tot line =" , cnt

start = 1
intr = 0
flag = 0
req = urllib2.Request("https://en.wikipedia.org/wiki/List_of_cakes")
response = urllib2.urlopen(req)
parser.feed(response.read())
print "tot line =" , cnt

cnt = 0
out = open("list.txt","w")
for item in L:
	cnt = cnt + 1
	out.write(str(cnt) + "," + item + "\n")
out.flush()
out.close()

	