from django.contrib import admin
from main.models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'photo','job','phone']
    list_display_links = ['id', 'user']

admin.site.register(Profile, ProfileAdmin)

class MeetingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'obj', 'previous_meeting','next_meeting']
    list_display_links = ['id', 'title']

admin.site.register(Meeting, MeetingAdmin)


class TranscriptionAdmin(admin.ModelAdmin):
    list_display = ['id','author', 'meeting','info','date_posted','last_modified']
    list_display_links = ['id', 'info']

admin.site.register(Transcription, TranscriptionAdmin)
