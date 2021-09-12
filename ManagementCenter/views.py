from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from .forms import *
from .models import *


def home(request):
    return render(request, 'home.html')

def set_hr_user(request):
    
    if ManagementCenter.objects.all()[0].CEO == request.user :
        if request.method == 'POST':
            form = SetHRForm(request.POST or None, instance=ManagementCenter.objects.all()[0])
            if form.is_valid():
                form.save()

        return render(request, 'set_HR_User.html', {'form': SetHRForm(instance=ManagementCenter.objects.all()[0]) })
    
    else:
        return render(request, 'access_denied.html')



def set_accounter_user(request):
    
    if ManagementCenter.objects.all()[0].CEO == request.user :
        if request.method == 'POST':
            form = SetAccounterForm(request.POST or None, instance=ManagementCenter.objects.all()[0])
            if form.is_valid():
                form.save()

        return render(request, 'set_Accounter_User.html', {'form': SetAccounterForm(instance=ManagementCenter.objects.all()[0]) })
    
    else:
        return render(request, 'access_denied.html')


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('home')

    else:
        return render(request, 'createUser.html', {'form': UserForm, })


def add_group_admin(request):
    if request.user in ( ManagementCenter.objects.all()[0].CEO, ManagementCenter.objects.all()[0].HR )  :
        if request.method == 'POST':
            form = GroupAdminForm(request.POST or None)
            if form.is_valid():
                form.save()

        return render(request, 'Aad_group_admin.html', {'form': GroupAdminForm })
    
    else:
        return render(request, 'access_denied.html')


def add_group_user(request):
    if request.user in ( ManagementCenter.objects.all()[0].CEO, ManagementCenter.objects.all()[0].HR )  :
        if request.method == 'POST':
            form = GroupUserForm(request.POST or None)
            if form.is_valid():
                form.save()

        return render(request, 'Aad_group_user.html', {'form': GroupUserForm })
    
    else:
        return render(request, 'access_denied.html')


def add_departement(request):
    
    if request.user in ( ManagementCenter.objects.all()[0].CEO, ManagementCenter.objects.all()[0].HR )  :
        if request.method == 'POST':
            form = DepartementForm(request.POST or None)
            if form.is_valid():
                form.save()

        return render(request, 'Aad_departement.html', {'form': DepartementForm })
    
    else:
        return render(request, 'access_denied.html')

def add_group(request):
    
    if request.user in ( ManagementCenter.objects.all()[0].CEO, ManagementCenter.objects.all()[0].HR )  :
        if request.method == 'POST':
            form = GroupForm(request.POST or None)
            if form.is_valid():
                form.save()

        return render(request, 'Aad_group.html', {'form': GroupForm })
    
    else:
        return render(request, 'access_denied.html')
