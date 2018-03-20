# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import *
from .forms import *
from django.contrib.auth import update_session_auth_hash

# Create your views here.

#session['is_student'] is true if logged in user is student 


@login_required
def index(request):

	print request.session['user_type']
	# print request.session['is_student']
	return render(request, 'HMSApp/dash.html')
	


class LoginView(View):
	form_class = UserLoginForm
	template_name = 'HMSApp/login.html'

	def get(self, request):
		if request.user.is_authenticated():
			return redirect("HMSApp:index")
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = self.form_class(request.POST)
		
		if form.is_valid():
			# user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			# user.set_password(password)
			# user.save()
			# print "User created"
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					if hasattr(request.user,"student"):
						# print request.user.student
						request.session['user_type'] = "student"
					if hasattr(request.user,"hosteladmin"):
						request.session['user_type'] = "hosteladmin"
					if(request.GET.get('next')):
						print "Here"
						return redirect(request.GET['next'])
					return redirect('HMSApp:index')
			else:
				error_msg = "Wrong Login Credentials! "
				print "Login unsuccessful"
				return render(request, "HMSApp/login.html", {'error_msg': error_msg})

		else:
			error_msg = "Wrong Login Credentials! "
			print "Login unsuccessful"
			return render(request, "HMSApp/login.html", {'error_msg': error_msg})			



class LogoutView(View):
	def get(self, request):
		if request.user.is_authenticated():
			logout(request)
			return redirect('login')
		


class ChangePasswordView(View):

	form_class = ChangePasswordForm
	def get(self, request):
		form = self.form_class()
		
		return render(request, 'HMSApp/change_password.html', {'form':form})
	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			# print form.cleaned_data['new_password']
			if form.cleaned_data['new_password'] != form.cleaned_data['confirm_password']:
				error_msg = 'New Password and Confirm Password Fields do not match!'
				return render(request, 'HMSApp/change_password.html', {'error_msg':error_msg, 'form':form,'color':'red'})


			if request.user.check_password(form.cleaned_data['old_password']):
				request.user.set_password(form.cleaned_data['new_password'])
				request.user.save()
				update_session_auth_hash(request, request.user)  
				return render(request, 'HMSApp/change_password.html', {'error_msg':'Password Changed Successfully', 'form':self.form_class(),'color':'green'})
			else:
				error_msg = 'Wrong Password! Please enter your correct password'
				return render(request, 'HMSApp/change_password.html', {'error_msg':error_msg, 'form':form, 'color':'red'})
		else:
			print "Form invalid"

#only for student
class RoomAllotmentView(View):

	def get(self, request):
		form = ProfileForm(instance=request.user.student)
		room_preference_form = RoomAllotmentForm
		request_status = RoomAllotment.objects.filter(student=request.user.student)
		# print request_status[0].preferred_block
		return render(request, 'HMSApp/room_allotment.html', {'form':form, 'preference_form':room_preference_form, 'request_status':request_status})

	def post(self, request):
		form = RoomAllotmentForm(request.POST)
		new_request = form.save(commit=False)
		new_request.student = request.user.student
		new_request.status = "Approval Pending"
		new_request.save()
		return redirect('/hms/room_allotment')

	# print request.session['is_student']
	# return render(request, 'HMSApp/room_allotment.html')


class ProfileView(View):

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		if self.request.session['user_type']=="student":
			print self.request.session['user_type']
			self.form_class = ProfileForm
		if self.request.session['user_type']=="hosteladmin":	
			self.form_class = ProfileFormAdmin
		return super(ProfileView, self).dispatch(*args, **kwargs)

	def get(self, request):
		user_type = request.session['user_type']
		form = self.form_class(None,instance=getattr(request.user, user_type))
		# student = Student.objects.get(user=request.user)
		return render(request, 'HMSApp/profile.html', {'form':form})

	def post(self, request):
		user_type = request.session['user_type']
		form = self.form_class(request.POST, instance=getattr(request.user, user_type))
		new_profile = form.save(commit=False)
		# new_profile.user = request.user

		new_profile.save()
		return render(request, 'HMSApp/profile.html', {'form':form})		


class HostelComplaintsView(View):
	form_class = ComplaintForm
	def get(self, request):
		form = self.form_class
		complaints = Complaint.objects.filter(student=request.user.student)
		return render(request, 'HMSApp/complaints.html', {'form':form, 'complaints':complaints})

	def post(self, request):
		form = self.form_class(request.POST)
		complaint = form.save(commit=False)
		complaint.student = request.user.student
		complaint.status = "Pending"
		complaint.save()
		return redirect('/hms/complaints')

#only for admin
class AllApplicationsView(View):

	def get(self, request):
		
		form = RoomAllotmentFormAdmin
		all_applications = RoomAllotment.objects.all()
		hostel_blocks = HostelBlock.objects.all()
		return render(request, 'HMSApp/all_applications.html', {'form':form, 'applications':all_applications, 'hostel_blocks':hostel_blocks})

	def post(self, request, **kwargs):
		# print type(int(kwargs['req_id']))
		# obj = RoomAllotment.objects.get(pk=int(kwargs['req_id']))
		# obj.status = "Approved"
		# obj.save()
		obj = RoomAllotment.objects.get(pk=int(kwargs['req_id']))
		form = RoomAllotmentFormAdmin(request.POST,instance=obj)
		appl = form.save(commit=False)
		if appl.status == "Approval Pending":
			appl.allotted_block.allotted_rooms +=1
			appl.room_no = appl.allotted_block.allotted_rooms
			appl.allotted_block.save()
		appl.status = "Approved"
		appl.save()
		all_applications = RoomAllotment.objects.all()
		return redirect("/hms/applications/")
		

class NoticeBoardView(View):
	form_class = NoticeBoardForm
	def get(self, request):
		form = self.form_class
		all_notices = NoticeBoard.objects.all().order_by('-date')
		return render(request, 'HMSApp/notice_board.html', {'form':form,'notices':all_notices} )

	def post(self, request):
		form = self.form_class(request.POST)
		notice = form.save(commit=False)
		notice.save()
		return redirect('/hms/notice_board')


class AllComplaintsView(View):
	def get(self, request):
		
		all_complaints = Complaint.objects.all()
		# hostel_blocks = HostelBlock.objects.all()
		return render(request, 'HMSApp/all_complaints.html', {'all_complaints':all_complaints})

	def post(self, request, **kwargs):
		# print type(int(kwargs['req_id']))
		# obj = RoomAllotment.objects.get(pk=int(kwargs['req_id']))
		# obj.status = "Approved"
		# obj.save()
		obj = Complaint.objects.get(pk=int(kwargs['req_id']))
		# form = RoomAllotmentFormAdmin(request.POST,instance=obj)
		obj.status = "Addressed"
		obj.save()
		return redirect("/hms/all_complaints/")


class DownloadRoomAllotmentView(View):

	def get(self, request):
		student = request.user.student
		room_allotted = RoomAllotment.objects.filter(student=student)[0]
		return render(request, 'HMSApp/room_allotment_letter.html', {'student':student, 'room_allotted':room_allotted})
