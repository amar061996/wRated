from django.conf.urls import url,include
import views as account_views

urlpatterns=[

url(r'^employee$',account_views.register_employee,name="employee"),
url(r'^workplace$',account_views.register_workplace,name="workplace"),
#interface
url(r'^employee/home$',account_views.employee_home,name="empHome"),
url(r'^workplace/home$',account_views.workplace_home,name="wrkHome"),


#workplace features
url(r'workplace/(?P<id>\d+)/employees/$',account_views.workplace_employees,name="workEmp"),
url(r'workplace/(?P<id>\d+)/rating/$',account_views.workplace_rating,name="workRating"),
url(r'workplace/(?P<id>\d+)/review/$',account_views.workplace_employees,name="workReview"),
#workplace_data
url(r'workplace/data',account_views.get_data,name='workplace-data'),

#delete_employee
url(r'employee/(?P<id>\d+)/delete/$',account_views.delete_employee,name="deleteEmp"),

url(r'login',account_views.login_view,name='login'),
url(r'logout',account_views.logout_view,name='logout')
]