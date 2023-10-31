from django.contrib import admin

# Register your models here.
from .models import Department, Course, Material, Order

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Material)
admin.site.register(Order)