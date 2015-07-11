from django.shortcuts import render

# Create your views here.

from .models import Class, Student, Lesson

def home(request):
    """ This view shows a list of all classes in the database """
    classes = Class.objects.all()

    template = "home.html"
    context = {"classes": classes}
    return render(request, template, context)

def singleClass(request, pk):
    template = "singleClass.html"
    context = {}
    return render(request, template, context)
