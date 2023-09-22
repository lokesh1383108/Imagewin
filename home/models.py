from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class uploadimage(models.Model):
    location_image=models.FileField()
    location_name = models.CharField(max_length=30)
    
