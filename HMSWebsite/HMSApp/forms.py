from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *

# class UserForm(forms.ModelForm):
# 	password = forms.CharField(widget=forms.PasswordInput) 

# 	class Meta:
# 		model = User
# 		fields = ['username', 'email', 'password', 'first_name', 'last_name']
		# fields = "__all__"

class UserLoginForm(forms.Form):
	username = forms.CharField(max_length=150)
	password = forms.CharField(widget=forms.PasswordInput) 


class ProfileForm(ModelForm):
	class Meta:
		model = Student
		# fields = '__all__'
		exclude = ['user']
	


class ComplaintForm(ModelForm):
	class Meta:
		model = Complaint
		exclude = ['status', 'student']


class RoomAllotmentForm(ModelForm):
	class Meta:
		model = RoomAllotment
		exclude = ['student', 'allotted_block', 'status', 'room_no']

class RoomAllotmentFormAdmin(ModelForm):
	class Meta:
		model = RoomAllotment
		fields = ['allotted_block']


class ProfileFormAdmin(ModelForm):
	class Meta:
		model = HostelAdmin
		exclude = ['user']

class NoticeBoardForm(ModelForm):
	class Meta:
		model = NoticeBoard
		fields = '__all__'


class ChangePasswordForm(forms.Form):
	old_password = forms.CharField(widget=forms.PasswordInput())
	new_password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput())