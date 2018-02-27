# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Student(models.Model):
	# id = models.IntegerField(primary_key=True)
	user = models.OneToOneField(User, models.CASCADE)
	reg_no = models.CharField(max_length=10)
	branch = models.CharField(max_length=20)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	course = models.CharField(max_length=10)
	year = models.IntegerField()


# class HostelAdmin(models.Model):
# 	user = models.OneToOneField(User, models.CASCADE)
