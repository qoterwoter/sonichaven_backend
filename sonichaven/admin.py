from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_soundengineer', 'is_artist')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'is_soundengineer', 'is_artist')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональная инфомрация', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'profile_image', 'image_tag')}),
        ('Роли', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'is_soundengineer', 'is_artist', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',
                       'is_staff', 'is_superuser', 'is_soundengineer', 'is_artist', 'groups', 'user_permissions',
                       'phoneNumber'),
        }),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email')
    readonly_fields = ('image_tag',)
    ordering = ('id',)

admin.site.register(User, CustomUserAdmin)
