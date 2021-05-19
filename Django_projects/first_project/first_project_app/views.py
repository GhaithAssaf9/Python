from django.shortcuts import HttpResponse, redirect # add redirect to import statement
from django.http import JsonResponse
def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def creat(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")
    
def destroy(request):
    return redirect("/blogs")

def bonus(request):
    return JsonResponse({"title": "my first blog", "content": "ok, i'm done of this assaignment"})