from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def submitquery(request):
    query = request.GET['query']
    try:
        answer = eval(query)
        mydict = {
            'query':query,
            'answer':answer,
            'error':False
        }
    except:
        mydict = {
            'error' : True,
        }
    return render(request,'index.html',context=mydict)


def error_404_view(request,exception):
    return render(request,'404.html')
