from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    number=models.CharField(max_length=12)
    description=models.TextField()
    
class Blog(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField()
    authname=models.CharField(max_length=15)
    img=models.ImageField(upload_to='blog', blank=True, null=True)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)