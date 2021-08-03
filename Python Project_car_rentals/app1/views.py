from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from app1.models import *
import bcrypt
from datetime import date, datetime

# Login & register functions

def login_register(request):
    if 'register' in request.POST:
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        age = request.POST['age']
        city = request.POST['city']
        password = request.POST['password']
        errors = User.objects.register(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/signin')
        else:
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(first_name = fname, last_name = lname, email = email, password = pw_hash, age = age, city = City.objects.get(name = city))
            request.session['id'] = new_user.id
            request.session['fname'] = fname
            request.session['lname'] = lname
            return redirect('/')

    if 'login' in request.POST:
        errors2 = User.objects.login(request.POST)
        if len(errors2) > 0:
            for key, value in errors2.items():
                messages.error(request, value)
            return redirect('/signin')
        email = request.POST['emaill']
        password = request.POST['passwordd']
        x = User.objects.filter(email = email)
        user=x.first()
        if x:
            if bcrypt.checkpw(request.POST['passwordd'].encode(), user.password.encode()):
                request.session['id'] = user.id
                request.session['fname'] = user.first_name
                request.session['lname'] = user.last_name
                return redirect('/')
            return redirect('/signin')
        return redirect('/signin')
    return redirect('/signin')

def log_out(request):
    del request.session['id']
    del request.session['fname']
    del request.session['lname']
    return redirect('/')

def log(request):
    data = {
        'cities': City.objects.all()
    }
    return render(request, 'login.html', data)
###########################################################################3


def home(request):
    if 'id' in request.session:
        data = {
            'cities': City.objects.all(),
            'types': Car_Type.objects.all(),

            'user' :User.objects.get(id=request.session['id'])
        }
        return render(request,'index.html', data)

    else:
        data = {
            'cities': City.objects.all(),
            'types': Car_Type.objects.all(),
        }
        return render(request,'index.html', data)

def gallery(request):
    if 'id' in request.session:
        data = {
            'all': Car.objects.all(),
            'user': User.objects.get(id = request.session['id']),
        }
        return render(request,'gallery.html', data) 
    else:
        data = {
            'all': Car.objects.all(),
        }
        return render(request,'gallery.html', data) 

def book(request):
    if request.POST['car_type']:
        reserves = Reserve.objects.all()
        for x in reserves:
            p = x.pickup_time
            r = x.return_time
            s = datetime.strptime(request.POST['pdate'], "%Y-%m-%d").date()
            e = datetime.strptime(request.POST['rdate'], "%Y-%m-%d").date()
            if (p>s and p<e) or (r>s and r<e):
                c=x.car
                c.status=False
                c.save()
            else:
                c=x.car
                c.status=True
                c.save()
        city = City.objects.get(name = request.POST['city'])
        company = city.companies.first()
        car_type = Car_Type.objects.get(type=request.POST['car_type'])
        result_car = Car.objects.filter(type=car_type, company = company, status=True)
        data = {
            'all': Car.objects.all(),
            'result': result_car,
            'cities': City.objects.all(),
            'types': Car_Type.objects.all(),
        }
    else:
        reserves = Reserve.objects.all()
        for x in reserves:
            p = x.pickup_time
            r = x.return_time
            s = datetime.strptime(request.POST['pdate'], "%Y-%m-%d").date()
            e = datetime.strptime(request.POST['rdate'], "%Y-%m-%d").date()
            if (p>s and p<e) or (r>s and r<e):
                c=x.car
                c.status=False
                c.save()
            else:
                c=x.car
                c.status=True
                c.save()
        city = City.objects.get(name = request.POST['city'])
        company = city.companies.first()
        result_car = Car.objects.filter(company = company, status=True)
        data = {
            'all': Car.objects.all(),
            'result': result_car,
            'cities': City.objects.all(),
            'types': Car_Type.objects.all(),
        }
    return render(request,'car.html', data)


def sedan(request):
    c = Category.objects.get(name="Sedan")
    data = {
        'all': Car.objects.filter(cate=c)
    }
    return render(request,'gallery.html', data)
def luxury(request):
    c = Category.objects.get(name="Luxury")
    data = {
        'all': Car.objects.filter(cate=c)
    }
    return render(request,'gallery.html', data) 
def suv(request):
    c = Category.objects.get(name="SUV")
    data = {
        'all': Car.objects.filter(cate=c)
    }
    return render(request,'gallery.html', data)
def micro(request):
    c = Category.objects.get(name="Micro")
    data = {
        'all': Car.objects.filter(cate=c)
    }
    return render(request,'gallery.html', data) 


######################### Admin Feild #######################################
def carrr(request):
    data = {
        'all': Car.objects.all()
    }
    return render(request, 'add_car.html', data)

def add_car(request):
    if 'add_car' in request.POST:
        name = request.POST['name']
        car_number = request.POST['car_number']
        model = request.POST['model']
        photo = request.POST['photo']
        company = Company.objects.get(name = request.POST['company'])
        type = Car_Type.objects.get(type = request.POST['type'])
        cate = Category.objects.get(name = request.POST['cate'])
        price=request.POST["price"]
        Car.objects.create(name=name, car_number=car_number, model=model, photo=photo, type=type, company=company, cate=cate,price=price)
        return redirect('/carrr')
    if 'pricee' in request.POST:
        id = request.POST['id']
        car = Car.objects.get(id=id)
        car.price = request.POST['price']
        car.save()
        return redirect('/carrr')

########################################## End Admin Feild ######################################################################
def account(request):
    data={
        'user' :User.objects.get(id=request.session['id']),
    }
    return render(request,"account.html", data)
    

# def details(request, num):
#     if 'id' in request.session:
#         car = Car.objects.get(id = num)
#         data = {
#             'all': Car.objects.all(),
#             'car': car,
#             'user': User.objects.get(id = request.session['id']),
#         }
#     else:
#         car = Car.objects.get(id = num)
#         data = {
#             'all': Car.objects.all(),
#             'car': car
#         }
#     return render(request, 'car_details.html', data)


# def reserve(request):
#     return render(request,'reservation.html')


# Not the details Function:
def details(request, id):
    if 'id' in request.session:
        car=Car.objects.get(id=id)
        context={
            'all':Car.objects.all(),
            'car':car,
            'user':User.objects.get(id =request.session['id']),
        }
    else:
        car=Car.objects.get(id=id)
        context={
            'all':Car.objects.all(),
            'car':car,
        }
    return render(request,'car_details.html', context)

# the reservation function:

def reservation(request, id):
    # carr=Car.objects.get(id=id)
    # context={
    #     'car':carr,
    # }
    # if 'reserve' in request.POST:
    # user=User.objects.get(id=request.session['id'])
    car=Car.objects.get(id=id)
    # pickup_time=request.POST['pdate']
    # return_time=request.POST['rdate']
    # company = Company.objects.get(name = request.POST['company'])
    # x = Reserve.objects.create(user=user, car=car, pickup_time=pickup_time, return_time=return_time, company=company)
    if 'id' in request.session:
        
        car=Car.objects.get(id=id)
        context={
            'cities': City.objects.all(),
            'all':Car.objects.all(),
            'car':car,
            'user':User.objects.get(id =request.session['id']),
            # 'res': x,
        }
        return render(request,'reservation.html', context)
    else:
        # car=Car.objects.get(id=id)
        # context={
        #     'all':Car.objects.all(),
        #     'car':car,
        # }
        return redirect('/login')


    # return render(request,'reservation.html', context)
    
def thanks(request,id):
    user=User.objects.get(id=request.session['id'])
    car=Car.objects.get(id=id)
    pickup_time=request.POST['pdate']
    return_time=request.POST['rdate']
    company = car.company
    x = Reserve.objects.create(user=user, car=car, pickup_time=pickup_time, return_time=return_time, company=company)
    return render(request,'thanks.html')


def about(request):
   
    return render(request,"about_us.html")