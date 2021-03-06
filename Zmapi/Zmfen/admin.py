from django.contrib import admin

# Register your models here.
from .models import CustsomerManager,Bank

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import CustsomerManager


class ProfileInline(admin.StackedInline):
    model = CustsomerManager
    max_num = 1
    can_delete = False

class UserProfileAdmin(UserAdmin):
    inlines = [ProfileInline, ]

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
admin.site.register(Bank)