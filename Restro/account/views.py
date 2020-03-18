from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Profile,Address
from django.contrib.auth.models import auth,User
# Create your views here.
def login(req):
	if req.user.is_authenticated:
		return redirect("/foodie")
	if req.method=="POST":
		email_or_tel=req.POST['email_or_tel']
		pwd=req.POST['pwd']
		user=auth.authenticate(username=email_or_tel,password=pwd)
		if user is not None:
			auth.login(req,user)
			return redirect("/foodie")
		else:messages.error(req,"User Not Found")
	return render(req,"account/login.html")
def logout(req):
	if req.user.is_authenticated:
		auth.logout(req)
		return redirect("/account/login")
def register(req):
	if req.user.is_authenticated:
		return redirect("/foodie")
	if req.method=="POST":
		fname=req.POST['fname']
		lname=req.POST['lname']
		email=req.POST['email']
		tel=req.POST['tel']
		pwd=req.POST['pwd']
		cnfpwd=req.POST['cnfpwd']
		if pwd != cnfpwd:
			messages.error(req,"Confirm password not match")
		else:
			user=User.objects.create_user(username=fname,first_name=fname,last_name=lname,email=email,password=pwd)
			profile=Profile.objects.create(user=user,tel=tel)
			auth.login(req,user,backend='django.contrib.auth.backends.ModelBackend')
			return redirect("/foodie")
	return render(req,"account/register.html")