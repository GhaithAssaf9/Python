from django.shortcuts import render, HttpResponse, redirect
from dojo_ninjas_app.models import dojos,ninjas

def index(request):
    if "nd" not in request.session:
        request.session['nd'] = []
    context = {
        "dojo": dojos.objects.all(),
        "ninja": ninjas.objects.all()
    }
    return render(request, 'htmll.html', context)

def add_dojo(request):
    new_dojo = dojos.objects.create(name= request.POST['name'], city= request.POST['city'], state= request.POST['state'], desc="Unknown")
    request.session['nd'].append(new_dojo.name)
    return redirect('/')

def add_ninja(request):
    new_ninja = ninjas.objects.create(first_name= request.POST['first_name'], last_name= request.POST['last_name'], dojo= dojos.objects.get(name= request.POST['select']))
    return redirect('/')

def reset(request):
    dojos.objects.all().delete()
    ninjas.objects.all().delete()
    return redirect('/')