from django.contrib import admin
from django.urls import path, include
from import_export.admin import ImportExportModelAdmin
from .models import Record, Comment, Folder, File, create_folder, Almene_kvoter
from django.db.models.signals import post_save

class RecordAdmin(ImportExportModelAdmin):
    pass

class CommentAdmin(ImportExportModelAdmin):
    pass

class FolderAdmin(ImportExportModelAdmin):
    pass

class FileAdmin(ImportExportModelAdmin):
    pass

class Almene_kvoterAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Record, RecordAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Folder, FolderAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Almene_kvoter, Almene_kvoterAdmin)

path('', include('crm.urls'))
