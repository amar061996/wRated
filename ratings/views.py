from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def rating_home(request):

	if request.method=="POST":
		print request.POST
		print request.POST.get('environment')
		print request.POST.get('sanitation')
		print request.POST.get('workload')
		print request.POST.get('cooperation')
		print request.POST.get('management')
		print request.POST.get('judicial')
		
		return HttpResponse("ok")
	return render(request,"ratings/rform.html")