from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Company
from .forms import CompanyNameForm, UpdateUserForm

def index(request):
    if request.user.is_authenticated:
        return redirect("sections/")
    else:
        return redirect('login')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    template = loader.get_template('template/login.html')
    context = {}
    if user is not None:
        login(request, user)
    return HttpResponse(template.render(context, request))

def logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/accounts/login')
def sections(request):
    template = loader.get_template('crms/sections.html')
    context = { 'sections':True }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/accounts/login')
def companies(request):
    companies_list = Company.objects.all()
    template = loader.get_template('crms/companies.html')
    context = { 'companies_list':companies_list }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/accounts/login')
def addcompany(request):
    if request.method == 'POST':
        form = CompanyNameForm(request.POST)
        if form.is_valid():
            Company.objects.create(company_name = form.data['company_name'], company_contact = form.data['company_contact'])
            template = loader.get_template('crms/addcompany.html')
            context = {}
            return redirect('companies')
    else:
        form = CompanyNameForm()
    template = loader.get_template('crms/addcompany.html')
    context = {}
    return HttpResponse(template.render(context, request))

@login_required(login_url='/accounts/login')
def users(request):
    users_list = User.objects.all()
    template = loader.get_template('crms/users.html')
    context = { 'users_list':users_list }
    return HttpResponse(template.render(context, request))

@staff_member_required
def update(request, target_id):
    template = loader.get_template('crms/update.html')
    if User.objects.filter(id=target_id).exists():
        target = User.objects.get(id=target_id)
        
    
        if request.method == "POST":
            form = UpdateUserForm(data=request.POST, instance=target)
            if form.is_valid:
                user = form.save(commit=False)
                user.save()
                return redirect('users')
        else:
            form = UpdateUserForm(instance=target)
        context = { 'form':form, 'user':target }
    else: 
        context = {'noUser':True}
        return redirect('users')
    
    return HttpResponse(template.render(context, request))
