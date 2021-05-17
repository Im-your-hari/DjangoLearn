from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    print(request.user.is_authenticated)
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')