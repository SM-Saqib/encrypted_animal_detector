from django.db import models

# Create your models here.
class Animal_images(models.Model):
    name=models.CharField(max_length=255)
    species=models.CharField(max_length=255)
    image=models.ImageField(upload_to ='uploads/')
