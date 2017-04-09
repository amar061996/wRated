from django.contrib import admin

# Register your models here.
from .models import Category,Workplace,Employee


admin.site.register(Category)
admin.site.register(Workplace)
admin.site.register(Employee)