from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from homepage.models import CustomUser
# Register your models here.

admin.site.register(CustomUser)
