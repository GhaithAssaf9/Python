from django.db import models
import re
import bcrypt

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

    def post(self, postData):
        errors3 = {}
        if  len(postData['post']) < 5:
            errors3["post"] = "Your post should be at least 5 characters"
        return errors3


class users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.TextField(max_length=500)
    password = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class though(models.Model):
    post = models.TextField(max_length=1000)
    user = models.ForeignKey(users, related_name="posts", on_delete = models.CASCADE)
    users_like = models.ManyToManyField(users, related_name="post_like")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

