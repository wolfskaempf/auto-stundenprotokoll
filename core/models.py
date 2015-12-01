from django.db import models

# Create your models here.


class Class(models.Model):

  """ This model contains information about the given class """
  name = models.CharField(max_length=100)
  teacher = models.CharField(max_length=100)
  identifier = models.CharField(max_length=100)
  subject = models.CharField(max_length=100)
  lastPaid = models.DateField(auto_now_add=False)
  remarks = models.TextField(blank=True)

  def __unicode__(self):
    # This function defines what the object will return when it's viewed as a
    # whole.
    return self.name + " " + self.subject

  class Meta:
    verbose_name_plural = "Classes"


class Student(models.Model):

  """ This model contains information about the student itself. """
  firstName = models.CharField(max_length=100)
  lastName = models.CharField(max_length=100)
  # This is the class the student is in. It's not possible to just use "class" as the name for this ManyToManyField
  # as it conflicts with python.
  inClass = models.ManyToManyField(Class)

  def __unicode__(self):
    # This function defines what the object will return when it's viewed as a
    # whole.
    return self.firstName + " " + self.lastName


class Lesson(models.Model):

  """ This model contains the protocol text of a given lesson in a class """
  inClass = models.ForeignKey(Class)
  date = models.DateField(auto_now_add=False)
  attendingStudents = models.ManyToManyField(Student, blank=True)
  protocol = models.TextField()

  def __unicode__(self):
    # This function defines what the object will return when it's viewed as a
    # whole.
    return self.protocol
