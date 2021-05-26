from django.db import models
import re

class ShowsManager(models.Manager):
    def basic_validator(self, postData):    
        errors = {}
        # EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # if not EMAIL_REGEX.match(postData['email']):
        #     errors['email'] = "Invalid email address!"
        
        if  len(postData['title'])<2 or not postData['title'].isalpha():
            errors["title"] = "Title should be at least 2 charecters and contains letters only"

        if len(postData['network']) < 3 or not postData['network'].isalpha():
            errors["network"] = "Network should be at least 3 charecters and contains letters only"

        if len(postData['desc']) < 10 or not postData['desc'].isalpha():
            errors["desc"] = "Description should be at least 10 charecters and contains letters only"

        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()



