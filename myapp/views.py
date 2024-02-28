from django.shortcuts import render
from django.http import HttpResponse
from .product import Products


def home(request):
    products =Products.objects.all()
    return render(request,'index.html',{'products':products})