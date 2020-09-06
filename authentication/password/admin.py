from django.contrib import admin

# Register your models here.
from password.models import UserInfo
admin.site.register(UserInfo)
