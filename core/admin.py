from django.contrib import admin
from core.models import Course, Subject, Profile



class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on',)
    
admin.site.register(Course, ProfileAdmin)
admin.site.register(Subject, ProfileAdmin)
admin.site.register(Profile, ProfileAdmin)