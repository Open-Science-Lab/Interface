from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import ArrayField



# Create your models here.


class operation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    operation_type=models.CharField(max_length=100)
    arguments=models.JSONField()


class operationV2(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    operation_type=models.CharField(max_length=100)
    arguments=ArrayField(models.CharField(max_length=200), blank=True)


class beaker(models.Model):
    str=models.CharField(max_length=250)


class stream(models.Model):
    lab_id=models.CharField(max_length=250)
    video_streams=models.JSONField()

class experiment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lab_id = models.CharField(max_length=110)
    equipments = ArrayField(models.CharField(max_length=200), blank=True)
    stream = ArrayField(models.CharField(max_length=200), blank=True)
    markers = ArrayField(models.CharField(max_length=200), blank=True)
    reactants = ArrayField(models.CharField(max_length=250), blank=True)