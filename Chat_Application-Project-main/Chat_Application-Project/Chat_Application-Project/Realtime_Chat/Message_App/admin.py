from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Team, Channel, DirectMessageThread, Message

# Register the custom user model with admin


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'email', 'is_online', 'last_seen', 'is_staff', 'is_active')
    list_filter = ('is_online', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)


admin.site.register(User, UserAdmin)
admin.site.register(Team)
admin.site.register(Channel)
admin.site.register(DirectMessageThread)
admin.site.register(Message)
