from django.shortcuts import render

# Create your views here.

from .models import Class, Student, Lesson

def home(request):

    classes = Class.objects.order_by(Class.name)

    template = "home.html"
    context = {"classes": classes}
    return render(request, template, context)

def singleClass(request, pk):
    template = "singleClass.html"
    context = {}
    return render(request, template, context)
