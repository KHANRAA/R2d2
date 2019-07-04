from django.shortcuts import render,HttpResponse,redirect
from movies.models import *

def homepage(request):
    return  render(request,'search.html')

def results(request):
    m=Movie()
    if request.GET.get('query') is not None:
        searchname=request.GET.get('query')
        res=m.getMovie(searchname)
        return render(request,'search.html',{'res':res,'search':True})
    else:
        return render(request,'search.html')

