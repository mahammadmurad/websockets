from django.contrib import admin
from .models import Message, UserChannel

admin.site.register(Message)
admin.site.register(UserChannel)

# Register your models here.
