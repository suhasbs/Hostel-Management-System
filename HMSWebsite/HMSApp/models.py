# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Student(models.Model):
	# id = models.IntegerField(primary_key=True)
	user = models.OneToOneField(User, models.CASCADE)
	reg_no = models.CharField(max_length=10, blank=True)
	branch = models.CharField(max_length=20,blank=True)
	first_name = models.CharField(max_length=50,blank=True)
	last_name = models.CharField(max_length=50,blank=True)
	course = models.CharField(max_length=10,blank=True)
	year = models.IntegerField(blank=True, null=True)

	def __str__(self):
		# return self.first_name+" "+self.last_name
		return self.user.username

class HostelAdmin(models.Model):
	user = models.OneToOneField(User, models.CASCADE)
	designtion = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	def __str__(self):
		return self.first_name+" "+self.last_name

class HostelBlock(models.Model):
	block_name = models.CharField(max_length=50)
	occupancy = models.IntegerField()
	total_rooms = models.IntegerField()
	allotted_rooms = models.IntegerField()
	def __str__(self):
		return self.block_name



class Complaint(models.Model):
	subject = models.CharField(max_length=255)
	complaint = models.TextField()
	status = models.CharField(max_length=50)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True, null=True)


class RoomAllotment(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	preferred_block = models.ForeignKey(HostelBlock, on_delete=models.CASCADE, related_name='preference')
	allotted_block = models.ForeignKey(HostelBlock, on_delete=models.CASCADE, related_name='allotted', null=True)
	status = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now_add=True, null=True)

