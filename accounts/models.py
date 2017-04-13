from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,UserManager

# Create your models here.

def upload_location(instance,filename):

	return "%s/%s"%(instance.id,filename)


class Category(models.Model):
	
	cname=models.CharField(max_length=250)

	def __str__(self):
		return self.cname

GENDER_CHOICES=(
	
	('Male','Male'),
	('Female','Female'),
	('Others','Others')
)

class Workplace(User):
	address=models.TextField(max_length=250)
	logo=models.ImageField(upload_to=upload_location,null=True,blank=True)
	wcategory=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Category')
	description=models.TextField(null=True,blank=False)



class Employee(User):
	profile_picture=models.ImageField(upload_to=upload_location,null=True,blank=True)
	gender=models.CharField(max_length=250,choices=GENDER_CHOICES,blank=False,default='Male')
	employee_id=models.CharField(max_length=250)
	eworkplace=models.ForeignKey(Workplace,on_delete=models.CASCADE,verbose_name='Workplace',blank=False)
