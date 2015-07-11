from django.shortcuts import render

# Create your views here.

def home(request):
    template = "home.html"
    context = {}
    return render(request, template, context)

def singleClass(request, pk):
    template = "singleClass.html"
    context = {}
    return render(request, template, context)
