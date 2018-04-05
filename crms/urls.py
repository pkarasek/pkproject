from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    
    url(r'^sections/', views.sections, name='sections'),
    url(r'^companies/', views.companies, name='companies'),
    url(r'^addcompany/', views.addcompany, name='addcompany'),
    url(r'^users/', views.users, name='users'),
    url(r'^update/(?P<target_id>\d+)', views.update, name='update'),

   # path('', views.index, name='index'),
   # path('sections/', views.sections, name='sections'),
   # path('companies/', views.companies, name='companies'),
   # path('addcompany/', views.addcompany, name='addcompany'),
   # path('users/', views.users, name='users'),
   # path('update/<int:target_id>', views.update, name='update'),

]
