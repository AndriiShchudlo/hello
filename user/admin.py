from django.contrib import admin

# Register your models here.
from user.models import BaseUser

admin.site.register(BaseUser)