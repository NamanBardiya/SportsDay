from django.shortcuts import render
from django.http import HttpResponse

def openpage(request):
    return render(request,"openpage.html")