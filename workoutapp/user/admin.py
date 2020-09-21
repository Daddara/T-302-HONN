from django.contrib import admin

# Register your models here.
from user.models import UserInfo, Messages

admin.site.register(UserInfo)
admin.site.register(Messages)