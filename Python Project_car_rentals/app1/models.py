from django.db import models
import re

from django.http import request
import bcrypt
from datetime import date,datetime


class UserManager(models.Manager):
    def register(self, postData):
        errors = {}
        if  len(postData['first_name']) < 2 or not postData['first_name'].isalpha():
            errors["first_name"] = "first name should be at least 2 chars and contains letters only"


        if len(postData['last_name']) < 2 or not postData['last_name'].isalpha():
            errors["last_name"] = "last name should be at least 2 chars and contains letters only"

        if len(postData['password']) < 8:
            errors["password"] = "password should be at least 8 characters"

        EMAILREGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+$')
        if not EMAILREGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"

        if postData['password'] != postData['cpassword']:
            errors["cpassword"] = "password should match password confirmation"
        return errors

    def login(self, postData):
        errors2 = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['emaill']):         
            errors2['emaill'] = "your email adress is not correct!"

        if len(postData['passwordd']) < 8:
            errors2["passwordd"] = "your login password shold be more than 8 charecters"
        return errors2

    # def payment(self, postData):
    #     errors3 = {}
    #     ######################################
    #     return errors3


class City(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

####################################################################
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.TextField(max_length=500)
    password = models.TextField(max_length=500)
    age = models.IntegerField()
    city = models.ForeignKey(City, related_name="users", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return self.first_name

########################################################################
class Company(models.Model):
    name = models.CharField(max_length=255)
    rate = models.IntegerField()
    email = models.TextField(max_length=500)
    password = models.TextField(max_length=500)
    cities = models.ManyToManyField(City, related_name="companies")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
#########################################################################
class Car_Type(models.Model):
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.type
#########################################################################
class Category(models.Model):
    name=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
#####################################################################
class Car(models.Model):
    name = models.CharField(max_length=255)
    car_number = models.IntegerField()
    model = models.IntegerField()
    photo = models.CharField(max_length=255)
    price = models.IntegerField()
    status = models.BooleanField()
    type = models.ForeignKey(Car_Type, related_name="cars", on_delete = models.CASCADE)
    company = models.ForeignKey(Company, related_name="cars", on_delete = models.CASCADE)
    cate = models.ForeignKey(Category, related_name="cars",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
####################################################################################
class Reserve(models.Model):
    user = models.ForeignKey(User, related_name="reserves", on_delete = models.CASCADE)
    car = models.ForeignKey(Car, related_name="reserves", on_delete = models.CASCADE)
    company = models.ForeignKey(Company, related_name="reserves", on_delete = models.CASCADE)
    pickup_time = models.DateField()
    return_time = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user
#############################################################################################
# class Payment(models.Model):
#     method = models.CharField(max_length=255)


def check_date(start,end):
    today = date.today()
    start = start
    end = end
    if today >= start and today <=end:
        return False
    return True

def car_status():
    reserves = Reserve.objects.all()
    for x in reserves:
        s = x.pickup_time
        e = x.return_time
        x.car.status = check_date(s,e)
    return 'Done'

def able():
    reserves = Reserve.objects.all()
    for x in reserves:
        p = x.pickup_time
        r = x.return_time
        print(p)
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
    return 'Done'

user = User.objects.get(id = 3)
car = Car.objects.get(id = 37)
company = Company.objects.get(name='Radwan')
p = date(2021, 6, 20)
r = date(2021, 6, 25)
res = Reserve.objects.create(user=user, car=car, company=company, pickup_time=p, return_time=r)

