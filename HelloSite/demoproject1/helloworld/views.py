from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, World!, from <i>Bobby Parsons</i> on <b>11/3/2021</b>')
# Create your views here.
