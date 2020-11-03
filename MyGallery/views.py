from django.http import HttpResponse
from django.shortcuts import render,redirect
from myapp.models import *

def show_home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    data = {'images':images,'cats':cats} 
    return render(request,'index.html',data)

def show_category_page(request,cid):
    print(cid)
    cats = Category.objects.all()
    category = Category.objects.get(pk=cid)
    print(category)

    images = Image.objects.filter(cat=category)
    data = {'images':images,'cats':cats}  
    return render(request,'index.html',data)

def show_about_page(request):    
    return render(request,"about.html",{})

def show_contact_page(request):
    contact_str ='hey, We are on Contact Us page'
    return HttpResponse(contact_str)
    
def home(request):
    return redirect('/home')