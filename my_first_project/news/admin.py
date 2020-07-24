from django.contrib import admin

from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_at', 'update_at', 'is_published', 'views']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']
    
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category', 'created_at', 'update_at')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

# admin.site.site_title = 'Управление новостями'
# admin.site.site_header = 'Управление новостями'
