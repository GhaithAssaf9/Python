from users_app.models import Users
from django.shortcuts import redirect, render, HttpResponse

def index(request):
    context = {
        "data": Users.objects.all()
    }
    return render(request, 'model.html', context)

def add(request):
    Users.objects.create(first_name= request.POST['fname'], last_name= request.POST['lastname'], email_adress= request.POST['email'], age= request.POST['age'])
 
    return redirect('/')

def delete(request):
    c = Users.objects.all()
    c.delete()
    return redirect('/')
