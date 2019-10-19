from django.http import HttpResponse
from django.shortcuts import render



def homepage(request):
    #return HttpResponse('homepage')
    return render(request,'homepage.html')

def about(request):
    #return HttpResponse('about')
    return render(request,'about.html')

def signin(request):
    #return HttpResponse('about')
    return render(request,'signin.html')

def createaccount(request):
    #return HttpResponse('about')
    return render(request,'createaccount.html')

def contactus(request):
    #return HttpResponse('about')
    return render(request,'contactus.html')
