from django.contrib import admin
from .models import *

admin.site.register(ManagementCenter)
admin.site.register(Departement)
admin.site.register(Group)
admin.site.register(GroupUser)
admin.site.register(GroupAdmin)
admin.site.register(EmployerAccount)
admin.site.register(CustomerAccount)