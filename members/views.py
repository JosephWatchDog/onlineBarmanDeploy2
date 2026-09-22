from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def bar(request):
    template = loader.get_template('baratmo.html')
    return HttpResponse(template.render())