from django.contrib import admin

from .models import Class, Lesson, Student
# Register your models here.

admin.site.register(Class)
admin.site.register(Lesson)
admin.site.register(Student)
