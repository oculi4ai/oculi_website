from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from django import forms
from .models import *


class SetHRForm(forms.ModelForm):
    class Meta:
        model   = ManagementCenter
        fields  = ('HR',)

class SetAccounterForm(forms.ModelForm):
    class Meta:
        model   = ManagementCenter
        fields  = ('Accounter',)

class DepartementForm(forms.ModelForm):
    class Meta:
        model   = Departement
        fields  = ('name','UserManager')

class GroupForm(forms.ModelForm):
    class Meta:
        model   = Group
        fields  = ('name', 'departement', 'UserManager')

class GroupAdminForm(forms.ModelForm):
    class Meta:
        model   = GroupAdmin
        fields  = ('user','Group')

class GroupUserForm(forms.ModelForm):
    class Meta:
        model   = GroupUser
        fields  = ('user','Group')



class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )

