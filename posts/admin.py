from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'owner', 'created_on', 'updated_on')
