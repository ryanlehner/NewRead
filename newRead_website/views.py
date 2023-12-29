from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def about(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'contact.html')