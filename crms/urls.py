from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    
    url(r'^sections/', views.sections, name='sections'),
    url(r'^companies/', views.companies, name='companies'),
    url(r'^addcompany/', views.addcompany, name='addcompany'),
    url(r'^users/', views.users, name='users'),
    url(r'^update/', views.update, name='update'),


]
