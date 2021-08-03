from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
from app1.models import *
import bcrypt

def log(request):
    return render(request, 'log.html')

def data(request):
    company = Company.objects.get(email=request.POST['emaill'], password=request.POST['passwordd'])
    if company in Company.objects.all():
        cars = Car.objects.filter(company=company)
        data = {
            'comp': company,
            'cars': cars,
        }
        return render(request, 'data.html', data)
    return redirect('/company')
