from django.conf.urls import url,include
import views as rating_views

urlpatterns=[

url(r'^$',rating_views.rating_home,name="home"),

]