from django.db import models
from __future__ import unicode_literals



class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        print(postData)
        if len(postData['title']) < 2:
            errors['title'] = "Title needs to be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = 'Network needs to be at least 3 characters'
        if len(postData['created_at']) < 8:
            errors['created_at'] = "Complete the release date field"
        if len(postData['desc']) < 10:
            errors['desc'] = "Description needs to be at least 10 characters"
        return errors



class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
def __repr__(self):
    return f"Show ID: ({self.id})| Title: {self.title}| Network: {self.network}| Release Date: {self.created_at}| Description: {self.desc} ||"