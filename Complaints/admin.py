from django.contrib import admin
from .models import Complaint
from import_export.admin import ImportExportActionModelAdmin

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'title', 'date')
    list_display_links = ('id','username', 'title')
    list_filter = ('username', 'title', 'date')
    search_fields = ('title', 'description', 'id', 'username', )

admin.site.register(Complaint, ComplaintAdmin)



