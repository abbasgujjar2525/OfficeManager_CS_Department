from django.contrib import admin
from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'title', 'date')
    list_display_links = ('id', 'username', 'title')
    list_filter = ('username', 'title', 'date')
    search_fields = ('title', 'description', 'id', 'username', 'first_name')


admin.site.register(Application, ApplicationAdmin)

