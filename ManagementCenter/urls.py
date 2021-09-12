from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [

    path('home/',               home, name= 'home' ),
    path('SetHR/',              set_hr_user, name= 'set_HR_page' ),
    path('SetAccounter/',       set_accounter_user, name= 'set_accounter_page' ),
    path('createUser/',         create_user, name= 'create_user_page'),

    path('addDepartement/',     add_departement, name= 'add_departement_page'),
    path('departement/<int:pk>/',edit_departement.as_view() , name='departement'),

    path('addGroup/',           add_group, name= 'add_group_page'),
    path('group/<int:pk>/' ,    edit_group.as_view() , name='group'),
        
    path('addGroupAdmin/',      add_group_admin, name= 'add_group_admin_page'),
    path('groupAdmin/<int:pk>/',edit_group_admin.as_view() , name='groupAdmin'),

    path('addGroupUser/',       add_group_user, name= 'add_group_user_admin'),
    path('groupUser/<int:pk>/', edit_group_user.as_view() , name='groupUser'),

    path(r'captcha/',           include('captcha.urls')),
]

