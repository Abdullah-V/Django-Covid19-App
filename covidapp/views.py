from django.shortcuts import Http404, render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
import requests
import json
# Create your views here.


def index(request):
    url = "https://api.covid19api.com/summary"
    result = requests.get(url)
    result = result.json()
    return render(request,'index.html',{'result':result})


def countryview(request,cn):
    url = "https://api.covid19api.com/dayone/country/"+cn
    result = requests.get(url)
    result = result.json()
    return render(request,'country.html',{'result':result,'cn':cn})
