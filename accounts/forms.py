from django import forms
from .models import Category,Workplace,Employee


class WorkplaceForm(forms.ModelForm):
	first_name=forms.CharField(max_length=250,label='Company Name')
	class Meta:
		model=Workplace
		fields=['first_name','username','email','password','address','logo','wcategory']
		exclude=['last_name']


class EmployeeForm(forms.ModelForm):
	employee_id=forms.CharField(max_length=250,label='ID number')
	class Meta:
		model=Employee
		fields=['username','first_name','last_name','email','password','employee_id','eworkplace']		