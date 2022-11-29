from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return HttpResponse('Hellow programmer')

def About(request):
    return HttpResponse('Hellow programmer, This is about page')

def contact(request):
    return HttpResponse(', This is contact  page')

