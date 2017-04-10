from django.shortcuts import render
from django.http import HttpResponse

#authentication
from django.contrib.auth import (
	authenticate,
	login,
	logout,
	get_user_model,


	)
# Create your views here.
from .forms import WorkplaceForm,EmployeeForm

def home(request):
	form=EmployeeForm()
	wform=WorkplaceForm()
	context={
	"form":form,
	"wform":wform,
	}
	return render(request,"index.html",context)

def register_employee(request):

	form=EmployeeForm(request.POST or None)
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