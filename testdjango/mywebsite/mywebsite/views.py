from django.http import HttpResponse
from django.shortcuts import render

# method view
def index(request):
	return render(request, 'index.html')

# def index2(request):

# 	title = "<h1>Ini adalah Home</h1>"
# 	title2 = "<h2>Selamat Datang di Website kami</h2>"
# 	result = title + title2
# 	return HttpResponse(result)

def about(request):
	# return HttpResponse("<h1>ini adalah about</h1>")
	return render(request, 'about.html')