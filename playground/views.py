from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse("Say hello")

def front_page(request):
    return HttpResponse("Front Page")

def hello_world(request):
    return HttpResponse("Hello World!")
