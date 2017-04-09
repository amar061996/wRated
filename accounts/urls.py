from django.conf.urls import url,include
import views as account_views

urlpatterns=[

url(r'^employee$',account_views.register_employee,name="employee"),
url(r'^workplace$',account_views.register_workplace,name="workplace"),
]