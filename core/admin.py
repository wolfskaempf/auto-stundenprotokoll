from django.contrib import admin

from .models import Class, LessonProtocol, Student
# Register your models here.

admin.site.register(Class)
admin.site.register(LessonProtocol)
admin.site.register(Student)
