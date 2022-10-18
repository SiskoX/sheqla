from django.contrib import admin

# Register your models here.
from .models import Room,Message

admin.site.register(Room)

class MessageAdmin(admin.ModelAdmin):
    list_display =['content','room','timestamp']

admin.site.register(Message,MessageAdmin)



