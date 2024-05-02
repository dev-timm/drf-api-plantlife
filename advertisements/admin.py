from django.contrib import admin
from .models import Advertisement

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):

    list_display = ('title', 'owner', 'availability', 'created_on', 'updated_on')
