#encoding=utf-8
from django.shortcuts import render,render_to_response

# Create your views here.
from django.http import HttpResponse
from handleData import func,myDict,size

def result(request):
	global func	,myDict
	info = ""
	data = []
	if (request.GET.has_key('q')):
		info = str(request.GET['q']).lower()
	if (request.GET.has_key('page')):
		page = int(request.GET['page'])
	else:
		page = 1
	infoList = info.split() #a list consists of words which will be searched
	tmp = []
	for i in range(1,size+1):
		g = 1
		for item in infoList:
			if not (item in myDict.keys()):
				g = 0
				break
			if str(i) in myDict[item]:
				g = 1
			else:
				g = 0
				break
		if g == 1:
			tmp.append(i)
	tot = 1
	if len(tmp) > 0:
		tot = len(tmp) / 10 + 1
	page = (page-1) % tot + 1
	for index in range(len(tmp)):
		if (index < 10 * (page-1) or index >= 10 * page):
			continue
		data.append({'name':func[tmp[index]],'url':str(tmp[index])})
	
	return render_to_response('result.html', {'data':data,'page':str(page)+"/"+str(tot),'lastpage':max(1,(page-1)),'nextpage':page+1,'info':info})
	
def foods(request):
	num = request.path[7:]
	httpfile = open("myapp/templates/%s.html" % num,"r")
	data = httpfile.read()
	httpfile.close()
	return HttpResponse(data)