from django.contrib import admin
from .models import Students
from import_export.admin import ImportExportActionModelAdmin

class StudentAdmin(ImportExportActionModelAdmin):
    list_display = ('first_name', 'last_name', 'rollno', 'date', 'isRegister')
    list_display_links = ('first_name', 'last_name', 'rollno', 'date')
    list_filter = ('section', 'batch', 'isRegister', 'date')
    search_fields = ('rollno', 'section', 'batch', 'username',)

admin.site.register(Students, StudentAdmin)
