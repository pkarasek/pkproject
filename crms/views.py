from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Company

def login(request):
    template = loader.get_template('crms/login.html')
    context = {}
    return HttpResponse(template.render(context, request))
