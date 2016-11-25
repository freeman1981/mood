from django.contrib import admin
from .models import Mood, MoodValues


class MoodAdmin(admin.ModelAdmin):
    pass
admin.site.register(Mood, MoodAdmin)


class MoodValuesAdmin(admin.ModelAdmin):
    pass
admin.site.register(MoodValues, MoodValuesAdmin)
