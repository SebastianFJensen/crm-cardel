from django.contrib import admin
from django.urls import path, include
from import_export.admin import ImportExportModelAdmin
from .models import Record, Comment, Folder, File

class RecordAdmin(ImportExportModelAdmin):
	pass
class CommentAdmin(ImportExportModelAdmin):
    pass



admin.site.register(Record,RecordAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Folder)
admin.site.register(File)
path('', include('crm.urls'))
