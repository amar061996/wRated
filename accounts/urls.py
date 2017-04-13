from django.conf.urls import url,include
import views as account_views

urlpatterns=[

url(r'^employee$',account_views.register_employee,name="employee"),
url(r'^workplace$',account_views.register_workplace,name="workplace"),
#interface
url(r'^employee/home$',account_views.employee_home,name="empHome"),
url(r'^workplace/home$',account_views.workplace_home,name="wrkHome"),
]