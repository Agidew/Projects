from django.shortcuts import render


def Home(request):
    return render(request,'home.html')

def About(request):
   return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

