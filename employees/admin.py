# employees/admin.py
from django.contrib import admin
from .models import Employee, Rating, Comment

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'department')
    search_fields = ('first_name', 'last_name', 'department')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('employee', 'rating_type', 'created_at')
    list_filter = ('rating_type', 'created_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('employee', 'text', 'created_at')
    search_fields = ('text',)

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
