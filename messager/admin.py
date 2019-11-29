from django.contrib import admin
from messager.models import Message
import django.contrib.auth.models
from django.contrib import auth


class MessageAdmin(admin.ModelAdmin):
    fields = ['email', 'message', 'date', 'sent', 'user']
    list_display = ('email', 'message', 'date', 'sent', 'user')


admin.site.register(Message, MessageAdmin)
admin.site.unregister(auth.models.Group)
