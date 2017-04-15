from django.shortcuts import render,redirect
from django.http import HttpResponse

#authentication
from django.contrib.auth import (
	authenticate,
	login,
	logout,
	get_user_model,


	)
# Create your views here.
from .forms import WorkplaceForm,EmployeeForm,UserLoginForm

def home(request):
	form=EmployeeForm()
	wform=WorkplaceForm()
	uform=UserLoginForm()
	context={
	"form":form,
	"wform":wform,
	'uform':uform,

	}

		
	
	return render(request,"index.html",context)

def register_employee(request):

	form=EmployeeForm(request.POST or None,request.FILES or None)
	if request.method=='POST':
		if form.is_valid():
			e_user=form.save(commit=False)
			password=form.cleaned_data.get("password")
			e_user.set_password(password)
			e_user.save()
			new_user=authenticate(username=e_user.username,password=password)
			login(request,new_user)
			return HttpResponse("Logged in as Employee")
	else:
		context={
		"form":form
		}		
		return render(request,"accounts/eform.html",context)

def register_workplace(request):

	form=WorkplaceForm(request.POST or None,request.FILES or None)
	if request.method=='POST':
		if form.is_valid():
			w_user=form.save(commit=False)
			password=form.cleaned_data.get("password")
			w_user.set_password(password)
			w_user.save()
			new_user=authenticate(username=w_user.username,password=password)
			login(request,new_user)
			return HttpResponse("Logged in as Employer")
	else:
		context={
		"form":form
		}		
		return render(request,"accounts/eform.html",context)


# employee interface

def employee_home(request):

	return render(request,"accounts/employee_interface.html")


def workplace_home(request):
	
	return render(request,"accounts/workplace_interface.html")	

def login_view(request):
	
	form=UserLoginForm(request.POST or None)
	if form.is_valid():
		username=form.cleaned_data.get("username")
		password=form.cleaned_data.get("password")
		user=authenticate(username=username,password=password)
		login(request,user)
		if hasattr(user,'employee'):
			return redirect("accounts:empHome")
		elif hasattr(user,'workplace'):
			return redirect("accounts:wrkHome")

		else:
			return HttpResponse("Hiii")	
		
