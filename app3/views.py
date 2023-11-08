from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def srinu(request):
    return HttpResponse('<h1><marquee>hi ra</marquee></h1>')
