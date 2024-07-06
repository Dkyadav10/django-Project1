from django.shortcuts import render
from django.http import HttpResponse, request

#create your views here......

def starting_page(request):
    return render(request,"DJANGO1/Project1/venv/my_site/blog/templates/blog/index.html")

def posts(request):
    pass

def post_detail(request):
    pass     


