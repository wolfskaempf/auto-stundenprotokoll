from django.contrib import admin

from .models import Class, Lesson, Student
# Register your models here.


class LessonAdmin(admin.ModelAdmin):
  # This defines what the Lesson Model should look like in the Django Admin
  list_display = ["date", "in_class", "protocol", ]
  search_fields = ["date", "in_class__name", "in_class__subject", "protocol", ]


class ClassAdmin(admin.ModelAdmin):
  # This defines what the Class Model should look like in the Django Admin
  list_display = ["name", "subject", "identifier", "last_paid", "teacher", ]
  search_fields = ["name", "subject", "identifier", "last_paid", "teacher", ]


class StudentAdmin(admin.ModelAdmin):
    # This defines what the Student Model should look like in the Django Admin
    list_display = ["first_name", "last_name",]
    search_fields = ["first_name", "last_name",]


# The following lines are responsible for making the Model Data that's
# inside the database available in the Django admin
admin.site.register(Class, ClassAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Student, StudentAdmin)
