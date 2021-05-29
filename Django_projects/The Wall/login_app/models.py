from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def register(self, postData):
#         errors = {}
#         # add keys and values to errors dictionary for each invalid field
#         if  len(postData['first_name']) < 2 or not postData['first_name'].isalpha():
#             errors["first_name"] = "first name should be at least 2 chars and contains letters only"


#         if len(postData['last_name']) < 2 or not postData['last_name'].isalpha():
#             errors["last_name"] = "last name should be at least 2 chars and contains letters only"

#         if len(postData['password']) < 8:
#             errors["password"] = "password should be at least 8 characters"

#         EMAILREGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+$')
#         if not EMAILREGEX.match(postData['email']):    # test whether a field matches the pattern
#             errors['email'] = "Invalid email address!"
        return errors

    # def login(self, postData):


class users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.TextField(max_length=500)
    password = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class messages(models.Model):
    post = models.TextField(max_length=1000)
    user = models.ForeignKey(users, related_name="messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class comments(models.Model):
    comment = models.TextField(max_length=1000)
    user = models.ForeignKey(users, related_name="comments", on_delete = models.CASCADE)
    message = models.ForeignKey(messages, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)