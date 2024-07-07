from django.shortcuts import render
from django.http import HttpResponse, request

#create your views here......

def starting_page(request):
    return render(request,"index.html")

def posts(request):
    pass

def post_detail(request):
    pass     


