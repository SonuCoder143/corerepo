from django.shortcuts import render

# Create your views here.

def firstView(request):
    return render(request,"html/first.html")

def secondView(request):
    return render(request,"html/second.html")