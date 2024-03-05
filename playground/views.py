from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    # return HttpResponse('Hello I am Rachit Poudel')
    return render(request, 'hello.html',{'address':'from KTM'})

def add(request):
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
    res = val1 + val2
    
    
    return render(request,'result.html',{'result':res})