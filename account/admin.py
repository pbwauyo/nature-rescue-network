from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser



class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'phone', 'first_name', 'last_name', 'date_joined', 'is_admin')
    search_fields = ('email', 'username')
    readonly_fields = ('last_login', 'date_joined')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    


admin.site.register(CustomUser, CustomUserAdmin)

