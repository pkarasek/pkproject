from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from django.contrib.auth.models import User

from .models import Company

def index(request):
    if request.user.is_authenticated:
        return redirect("sections/")
    else:
        return redirect("login/")

def login(request):
    template = loader.get_template('crms/login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def sections(request):
    template = loader.get_template('crms/sections.html')
    context = {}
    return HttpResponse(template.render(context, request))
