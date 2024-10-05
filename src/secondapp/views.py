from django.shortcuts import render

# Create your views here.

def thirdView(request):
    return render(request,"html/third.html")

def fourthView(request):
    return render(request,"html/fourth.html")