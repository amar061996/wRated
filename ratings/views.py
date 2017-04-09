from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def rating_home(request):

	if request.method=="POST":
		print request.POST
		print request.POST.get('new')
		
		return HttpResponse("ok")
	return render(request,"ratings/rform.html")