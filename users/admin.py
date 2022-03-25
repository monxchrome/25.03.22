from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'f_name', 'phone',)
    fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('PData', {'fields': ('f_name', 'l_name', 'phone', 'dt_birth')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    search_fields = ('email', )
    ordering = ('email', )
