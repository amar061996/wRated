from django.shortcuts import render,redirect,get_object_or_404
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
#models
from .models import Employee,Workplace
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
	if request.user.is_authenticated:
		if hasattr(request.user,'employee'):
		
			context={
			'emp':request.user.employee
			}
			return render(request,"accounts/employee_interface.html",context)
		else:
			return HttpResponse("Sign in As Employee")
	else:
	
		return HttpResponse("Sign in")		


#workplace

def workplace_home(request):
	if request.user.is_authenticated:
		if hasattr(request.user,'workplace'):
			context={
			'workp':request.user.workplace
			}
			return render(request,"accounts/workplace_interface.html",context)
		else:
			return HttpResponse("Sign in as Workplace")
	else:
		return HttpResponse("Sign in")				


#workplace-employees

def workplace_employees(request,id):
	workplace=get_object_or_404(Workplace,id=id)
	employee_list=Employee.objects.filter(eworkplace=workplace)
	
	context={
	"employee_list":employee_list
	}
	
	return render(request,"accounts/employee_list.html",context)


#workplace-rating

def workplace_rating(request,id):
	workplace=get_object_or_404(Workplace,id=id)
	print workplace
	return HttpResponse("This is workplace rating")

#workplace-review
def workplace_review(request,id):
	workplace=get_object_or_404(Workplace,id=id)
	print workplace
	return HttpResponse("This is workplace review")

#delete employee
def delete_employee(request,id):
	employee=get_object_or_404(Employee,id=id)
	if request.user.workplace==employee.eworkplace:
		employee.delete()
		return redirect("accounts:workEmp",id=request.user.workplace.id)
	else:
		return HttpResponse("Not authorised to delete the Employee")	
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
		

def logout_view(request):

	logout(request)
	return redirect("home")


