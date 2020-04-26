from django.contrib import admin
from .models import employees
from .models import students
# Register your models here.
admin.site.register(employees)
admin.site.register(students)

