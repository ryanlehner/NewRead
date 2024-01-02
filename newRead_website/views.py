from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# nav bar
# all are the same, just different ways to do things
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def about(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'contact.html')