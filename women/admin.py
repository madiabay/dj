from django.contrib import admin
from women.models import Women

# Register your models here.

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'time_create', 'time_update', 'is_published', 'cat')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


admin.site.register(Women, WomenAdmin)
