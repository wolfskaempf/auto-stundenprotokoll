from django.db import models

# Create your models here.
class Student(models.Model):
    """ This model contains information about the student itself. """
    firstName = Model.CharField(max_length=100)
    lastName = Model.CharField(max_length=100)
