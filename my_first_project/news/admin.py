from django.contrib import admin

from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'update_at', 'is_published']
    

admin.site.register(News, NewsAdmin)
