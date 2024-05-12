from django.shortcuts import render
from django.http import HttpResponse

def get_info(request):
    return HttpResponse("Hello World")

# Create your views here.
