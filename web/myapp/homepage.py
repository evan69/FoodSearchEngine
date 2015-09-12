#coding:utf8
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
def index(request):
	return render_to_response("homepage.html",{})
'''
	return HttpResponse("""<title>Food Search Engine</title>
<form method="GET" action="/search">
Please input: <input type="text" name="q">
<input type="submit"/>
</from>
""")
'''