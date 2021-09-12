from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [

    path('home/', home, name= 'home' ),
    path('SetHR/', set_hr_user, name= 'set_HR_page' ),
    path('SetAccounter/', set_accounter_user, name= 'set_accounter_page' ),
    path('addDepartement/', add_departement, name= 'add_departement_page'),
    path('addGroup/', add_group, name= 'add_group_page'),
    path('createUser/', create_user, name= 'create_user_page'),
    path('addGroupAdmin/', add_group_admin, name= 'add_group_admin_page'),
    path('addGroupUser/', add_group_user, name= 'add_group_user_admin'),
     path(r'captcha/', include('captcha.urls')),
]
