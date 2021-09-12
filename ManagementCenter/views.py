from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views.generic import ListView ,DetailView, UpdateView
from django.contrib.auth.models import User
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
            return render(request, 'createUser.html', {'form': UserForm(request.POST or None), 'message': form.errors })

    else:
        return render(request, 'createUser.html', {'form': UserForm, })


def add_group(request):
    
    if request.user in ( ManagementCenter.objects.all()[0].CEO, ManagementCenter.objects.all()[0].HR )  :
        if request.method == 'POST':
            form = GroupForm(request.POST or None)
            if form.is_valid():
                form.save()

        return render(request, 'Aad_group.html', {'form': GroupForm })
    
    else:
        return render(request, 'access_denied.html')



class edit_group(UpdateView):

	model=Group
	fields = [
        "name",
        "departement",
        "UserManager"
    ]

	def post(self, request, *args, **kwargs):
   	    if 'edit' in request.POST:
   	        G=Group.objects.get(pk=self.kwargs['pk'])
   	        form = GroupForm(request.POST, request.FILES , instance=G)			
   	        if form.is_valid():
   	            form.save()
   	        return redirect('group', G.pk)


   	    elif 'delete' in request.POST:
   	        G=Group.objects.get(pk=self.kwargs['pk'])
   	        G.delete()
   	        return redirect('home')



def add_group_admin(request):
    if request.user in ( ManagementCenter.objects.all()[0].CEO, ManagementCenter.objects.all()[0].HR )  :
        if request.method == 'POST':
            form = GroupAdminForm(request.POST or None)
            if form.is_valid():
                form.save()

        return render(request, 'Aad_group_admin.html', {'form': GroupAdminForm })
    
    else:
        return render(request, 'access_denied.html')


class edit_group_admin(UpdateView):

	model=GroupAdmin
	fields = [
        "user",
        "Group"
    ]

	def post(self, request, *args, **kwargs):
   	    if 'edit' in request.POST:
   	        GA=GroupAdmin.objects.get(pk=self.kwargs['pk'])
   	        form = GroupAdminForm(request.POST, request.FILES , instance=GA)			
   	        if form.is_valid():
   	            form.save()
   	        return redirect('groupAdmin', GA.pk)


   	    elif 'delete' in request.POST:
   	        GA=GroupAdmin.objects.get(pk=self.kwargs['pk'])
   	        GA.delete()
   	        return redirect('home')

			

def add_group_user(request):
    if request.user in ( ManagementCenter.objects.all()[0].CEO, ManagementCenter.objects.all()[0].HR )  :
        if request.method == 'POST':
            form = GroupUserForm(request.POST or None)
            if form.is_valid():
                form.save()

        return render(request, 'Aad_group_user.html', {'form': GroupUserForm })
    
    else:
        return render(request, 'access_denied.html')


class edit_group_user(UpdateView):

	model=GroupUser
	fields = [
        "user",
        "Group"
    ]

	def post(self, request, *args, **kwargs):
   	    if 'edit' in request.POST:
   	        GA=GroupUser.objects.get(pk=self.kwargs['pk'])
   	        form = GroupUserForm(request.POST, request.FILES , instance=GA)			
   	        if form.is_valid():
   	            form.save()
   	        return redirect('groupUser', GA.pk)


   	    elif 'delete' in request.POST:
   	        GA=GroupUser.objects.get(pk=self.kwargs['pk'])
   	        GA.delete()
   	        return redirect('home')





def add_departement(request):
    
    if request.user in ( ManagementCenter.objects.all()[0].CEO, ManagementCenter.objects.all()[0].HR )  :
        if request.method == 'POST':
            form = DepartementForm(request.POST or None)
            if form.is_valid():
                form.save()

        return render(request, 'Aad_departement.html', {'form': DepartementForm })
    
    else:
        return render(request, 'access_denied.html')




class edit_departement(UpdateView):

	model=Departement
	fields = [
        "name",
        "UserManager"
    ]

	def post(self, request, *args, **kwargs):
   	    if 'edit' in request.POST:
   	        D=Departement.objects.get(pk=self.kwargs['pk'])
   	        form = DepartementForm(request.POST, request.FILES , instance=D)			
   	        if form.is_valid():
   	            form.save()
   	        return redirect('departement', D.pk)


   	    elif 'delete' in request.POST:
   	        D=Departement.objects.get(pk=self.kwargs['pk'])
   	        D.delete()
   	        return redirect('home')
