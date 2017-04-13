from __future__ import unicode_literals

from django.db import models

# Create your models here.
from accounts.models import Workplace,Employee



class Rating(models.Model):
	environment=models.DecimalField(max_digits=2,decimal_places=1,default=0)
	sanitation=models.DecimalField(max_digits=2,decimal_places=1,default=0)
	workload=models.DecimalField(max_digits=2,decimal_places=1,default=0)
	cooperation=models.DecimalField(max_digits=2,decimal_places=1,default=0)
	management=models.DecimalField(max_digits=2,decimal_places=1,default=0)
	judicial=models.DecimalField(max_digits=2,decimal_places=1,default=0)
	score=models.DecimalField(max_digits=3,decimal_places=1)
	avg=models.DecimalField(max_digits=2,decimal_places=1)
	comments=models.TextField(null=True,blank=False)
	employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
	workplace=models.ForeignKey(Workplace,on_delete=models.CASCADE)
	created=models.DateTimeField(auto_now=False,auto_now_add=True)
