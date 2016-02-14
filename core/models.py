from django.db import models

# Create your models here.


class Class(models.Model):

  """ This model contains information about the given class """
  name = models.CharField(max_length=100)
  teacher = models.CharField(max_length=100)
  identifier = models.CharField(max_length=100)
  subject = models.CharField(max_length=100)
  last_paid = models.DateField(auto_now_add=False)
  remarks = models.TextField(blank=True)

  def __unicode__(self):
    # This function defines what the object will return when it's viewed as a
    # whole.
    return self.name + " " + self.subject

  class Meta:
    verbose_name_plural = "Classes"


class Student(models.Model):

  """ This model contains information about the student itself. """
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  # This is the class the student is in. It's not possible to just use "class" as the name for this ManyToManyField
  # as it conflicts with python.
  in_class = models.ManyToManyField(Class)

  def __unicode__(self):
    # This function defines what the object will return when it's viewed as a
    # whole.
    return self.first_name + " " + self.last_name


class Lesson(models.Model):

  """ This model contains the protocol text of a given lesson in a class """
  in_class = models.ForeignKey(Class)
  date = models.DateField(auto_now_add=False)
  attending_students = models.ManyToManyField(Student, blank=True)
  protocol = models.TextField()

  def __unicode__(self):
    # This function defines what the object will return when it's viewed as a
    # whole.
    return self.protocol
