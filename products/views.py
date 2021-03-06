from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import products,contacts
from .forms import ProductForm

def home(request):
    print(request.user.is_authenticated)
    
    return render(request,'home.html')

def about(request):
    my_context ={
        "name" : "hari",
        "email" : "baluoger91@gmail.com",
        "phone" : 8157096325,
        "skills" : ["html","css","java","c","python","django","javaScript"]
    }
    return render(request,'about.html',my_context)

def contact(request):
    return render(request,'contact.html')

def products_details(request,*args):
    obj = products.objects.all()
    prod_db = {
        "obj" : obj
    }
    return render(request,'products_details.html',prod_db)

def create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products')
    return render(request,'products_create.html',{'form':form})