from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'username', 'referral_code', 'first_name', 'last_name']
    list_editable = ['phone', 'username', 'referral_code', 'first_name', 'last_name']
    list_display_links = ['id']
    search_fields = ['phone', 'username', 'first_name', 'last_name']


admin.site.register(User, UserAdmin)
