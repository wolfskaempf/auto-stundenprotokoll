from django.shortcuts import render

# Create your views here.

from .models import Class, Student, Lesson


def home(request):
  """ This view shows a list of all classes in the database """
  classes = Class.objects.all()

  template = "home.html"
  context = {"classes": classes}
  return render(request, template, context)


def singleClass(request, pk, entries):
  """ This view is supposed to be printed once a month for the archive. It should reset itself after every "lastPaid" of any given class """
  if not entries:
      entries = 4

  activeClass = Class.objects.get(pk=pk)
  lessons = Lesson.objects.filter(inClass=pk).order_by("date").reverse()[:entries]

  template = "singleClass.html"
  context = {"class": activeClass, "lessons": lessons}
  return render(request, template, context)
