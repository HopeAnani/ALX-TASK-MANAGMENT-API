from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('id', 'name', 'email', 'is_active', 'is_staff', 'date_joined', 'last_login')
    search_fields = ('email', 'name')
    ordering = ('date_joined',)
    list_filter = ('is_active', 'is_staff')

    # Fieldsets define how fields appear in the admin
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )

admin.site.register(User, CustomUserAdmin)
