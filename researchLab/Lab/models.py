from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

# Create your models here.


class operation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    operation_type=models.CharField(max_length=100)
    arguments=models.JSONField()



class beaker(models.Model):
    str=models.CharField(max_length=250)