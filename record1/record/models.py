from django.db import models

# Create your models here.
class User(models.Model):
    cid = models.CharField(max_length=10,blank=True,null=True)
    cname = models.CharField(max_length=255)
    cemail = models.EmailField(max_length=255,unique=True)
    cname1 = models.CharField(max_length=255)
