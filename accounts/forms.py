from django import forms
from .models import Category,Workplace,Employee


class WorkplaceForm(forms.ModelForm):
	first_name=forms.CharField(max_length=250,label='Company Name')
	class Meta:
		model=Workplace
		fields=['first_name','description','username','email','password','address','logo','wcategory']
		exclude=['last_name']


class EmployeeForm(forms.ModelForm):
	employee_id=forms.CharField(max_length=250,label='ID number')
	class Meta:
		model=Employee
		fields=['username','first_name','last_name','gender','profile_picture','email','password','employee_id','eworkplace']		

		def __init__(self, *args, **kwargs):
			super(EmployeeForm, self).__init__(*args, **kwargs)
			for field in self.fields:
				field.widget.attrs.update({'class' : 'form-control'})