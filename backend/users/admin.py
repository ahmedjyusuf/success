from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib import admin
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin, UserChangeForm

# Register your models here.

# class CustomUserAdmin(UserAdmin):
#     model = User
#     form = UserChangeForm

#     fieldsets = (
#         *UserAdmin.fieldsets,
#         (
#             'User role',
#             {
#                 'fields': (
#                     'timezone',
#                 ),
#             }
#         ),
#     )

#     add_fieldsets = (
#         (
#             None,
#             {
#                 'classes': ('wide',),
#                 'fields': ('password1', 'password2', 'first_name', 'last_name', 'timezone', 'email'),
#             }
#         ),
#     )
#     ordering = ['email']


admin.site.register(User)
