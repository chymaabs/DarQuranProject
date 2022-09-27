from django.shortcuts import render

# Create your views here.
def welcome(request):
    from django.http import HttpResponse
    HttpResponse("Hello, world!")