from django.shortcuts import render,HttpResponse,redirect
from movies.models import Movie

def homepage(request):
    return  render(request,'search.html')

def results(request):
    m=Movie()
    if request.GET.get('query') is not None:
        searchName=request.GET.get('query')
        res=m.getMovie(searchName)
        return render(request,'search.html',{'res':res,'search':True})
    else:
        return render(request,'search.html')

