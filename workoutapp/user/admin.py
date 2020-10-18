from django.contrib import admin

# Register your models here.
from user.models import UserInfo, Messages, Follow, FriendRequest

admin.site.register(UserInfo)
admin.site.register(Messages)
admin.site.register(Follow)
admin.site.register(FriendRequest)