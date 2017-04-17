from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Rating



def calc_score(request):
	return (float(request.POST["environment"])+float(request.POST["sanitation"])+float(request.POST["workload"])+float(request.POST["cooperation"])+float(request.POST["management"])+float(request.POST["judicial"]))


def calc_avg(request):
	return calc_score(request)/6


def rating_home(request):

	if request.method=="POST":
		if request.user.is_authenticated:
			if hasattr(request.user,'employee'):
				employee=request.user.employee
				workplace=employee.eworkplace
				rating=Rating.objects.create(
					environment=request.POST["environment"],
					sanitation=request.POST["sanitation"],
					workload=request.POST["workload"],
					cooperation=request.POST["cooperation"],
					management=request.POST["management"],
					judicial=request.POST["judicial"],
					score=calc_score(request),
					avg=calc_avg(request),
					comments=request.POST['comment'],
					employee=employee,
					workplace=workplace
					)
				
				return HttpResponse("ok")
		else:
			return HttpResponse("Login")
	return render(request,"ratings/rform.html")