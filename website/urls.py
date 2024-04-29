from django.urls import path
from . import views 
from .views import AddCommentView, import_from_excel, create_new_folder, upload_file, EditCommentView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('Arkiveret/', views.archived, name='archived'),
    path('Prospekter/', views.prospects, name='prospects'),
    path('Leads/', views.lead, name='lead'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('Record/<int:pk>', views.customer_record, name='Record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('importrecorddata', views.ImportRecordData.as_view(), name='importrecorddata'),
    path('Record/<int:pk>/comment/', views.AddCommentView.as_view(), name='add_comment1'),
    path('import/', import_from_excel, name='import_from_excel'),
    path('create-folder/', views.create_new_folder, name ='create_new_folder'),
    path('folder/<int:pk>/', views.open_folder, name='open_folder'),
    path('upload-new-file', views.upload_file, name='upload_file'),
    path('record/<int:record_id>/comment/<int:comment_id>/edit/', views.EditCommentView.as_view(), name='edit_comment'),
    path('search/', views.search, name='search'),
    path('delete_file/<int:pk>/', views.delete_file, name='delete_file'),
] 
if settings.DEBUG:+ static(settings.MEDIA_URL, document_root=settings.AZURE_STORAGE_CONTAINER) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += [
        path('media/<path:path>', serve, {
            'document_root': f'{settings.AZURE_STORAGE_CONTAINER}/{settings.MEDIA_ROOT}',
            'show_indexes': True,
        }),
    ]
