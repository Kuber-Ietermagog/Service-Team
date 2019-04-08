from django.contrib import admin
from accounts.models import UserProfileInfo
from django.contrib.auth.models import Permission

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Permission)
