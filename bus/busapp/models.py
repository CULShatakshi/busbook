from django.db import models

# Create your models here.
class BusListItem(models.Model):
    content = models.TextField()
    last_name=models.TextField(null=True)
    date=models.DateField(null=True) 
    city=models.TextField(null=True)