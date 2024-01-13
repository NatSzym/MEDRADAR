# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser
# from .forms import CustomUserChangeForm, CustomUserCreationForm
#
#
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
#     ordering = ['email']
#
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal Info', {'fields': ('first_name', 'last_name', 'pesel', 'birth_date', 'gender')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#     )
#
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2'),
#         }),
#         ('Personal Info', {
#             'classes': ('wide',),
#             'fields': ('first_name', 'last_name', 'pesel', 'birth_date', 'gender'),
#         }),
#         ('Permissions', {
#             'classes': ('wide',),
#             'fields': ('is_active', 'is_staff', 'is_superuser'),
#         }),
#     )
#
#
# admin.site.register(CustomUser, CustomUserAdmin)
