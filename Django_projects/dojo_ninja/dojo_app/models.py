from django.db import models

class dojo(models.Model):
    name = models.CharField(max_length=45)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    desc=models.TextField(null=True)
 

class ninjas(models.Model):
    first_name = models.CharField(max_length=70)
    dojo = models.ForeignKey(dojo, related_name="ninjas", on_delete = models.CASCADE)
    last_name = models.CharField(max_length=70)




