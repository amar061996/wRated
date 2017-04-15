from django import forms
from .models import Category,Workplace,Employee
from django.contrib.auth import authenticate

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


class UserLoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)

	def clean(self,*args,**kwargs):
		username=self.cleaned_data.get("username")
		password=self.cleaned_data.get("password")

		
		if username and password:
			user=authenticate(username=username,password=password)
			if not user:
				raise forms.ValidationError("User does not exist")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect Password")
			if not user.is_active:
				raise forms.ValidationError("User not Active")

		return super(UserLoginForm,self).clean(*args,**kwargs)					