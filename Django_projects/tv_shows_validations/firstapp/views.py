from typing import Sequence
from django.shortcuts import render,redirect
from firstapp.models import Shows, ShowsManager
from django.contrib import messages
from firstapp.models import *

def main_page(request):
    return redirect('/shows')

def all_shows(request):
    if "add" in request.POST:
        errors = Shows.objects.basic_validator(request.POST)
        if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
        # redirect the user back to the form to fix the errors
            return redirect('/shows/new')
        Shows.objects.create(title = request.POST['title'], desc = request.POST['desc'], network = request.POST['network'], created_at = request.POST['date'])
    if 'update' in request.POST:
        errors = Shows.objects.basic_validator(request.POST)
        if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
        # redirect the user back to the form to fix the errors
            return redirect('/shows/new')

        # c = Shows.objects.get(id = request.session['id'])
        # c.title = request.POST['title']
        # c.desc = request.POST['desc']
        # c.network = request.POST['network']
        # c.created_at = request.POST['date']
        # c.save()
    context = {
        'shows': Shows.objects.all()
    }
    return render(request, 'all_shows.html', context)

def show_this_show(request, num):
    if 'update' in request.POST:
        errors = Shows.objects.basic_validator(request.POST)
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/shows/'+str(num)+'/edit')
    if 'update' in request.POST:
        c = Shows.objects.get(id = request.session['id'])
        c.title = request.POST['title']
        c.desc = request.POST['desc']
        c.network = request.POST['network']
        c.created_at = request.POST['date']
        c.save()
    context = {
        'this_show': Shows.objects.get(id=int(num))
    }
    return render(request, 'show_this.html', context)

def add_new(request):

    return render(request, 'add_show.html')

def edit(request, num):
    context = {
        'this_show': Shows.objects.get(id=int(num))
    }
    request.session['id'] = int(num)
    return render(request, 'edit.html', context)

def delete(request, num):
    c = Shows.objects.get(id=int(num))
    c.delete()
    return redirect('/shows')
