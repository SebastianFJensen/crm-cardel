@login_required
def folder(request,folderid=1):
    
    folder = get_object_or_404(Folder,id=folderid)
    files = File.objects.filter(folder=folder)
    if request.method == 'POST':
        file = request.FILES.get('uploadfile')
        filename = request.POST.get('filename')
        if file and filename:
            File.objects.create(filename=filename,file=file,folder=folder)
            return redirect(reverse('website:folder',kwargs={'folderid':folderid}))
    context = {
        'folder':folder,
        'files':files
    }
    return render(request,'website/folder.html',context)

@login_required
def deleteFolder(request,folderid):
    folder = get_object_or_404(Folder,id=folderid)
    folder.delete()
    messages.success(request,'Deleted successfully')
    return redirect('home')

@login_required
def addFolder(request):
    if request.method == 'POST':
        folder_name = request.POST.get('addfolder')
        description = request.POST.get('description')
        folder = Folder.objects.create(foldername=folder_name,folderuser=request.user,description=description)
        if folder:
            return redirect('home')
        else:
            messages.warning(request,'Folder is not created!')
            return redirect('home')

@receiver(post_save, sender=Record)
def create_folder(sender, instance=None, created=False, **kwargs):
    if created:
        foldername = instance.BFE_Nummer
        folder_path = os.path.join('media', 'folders', foldername)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        subfolder_names = ["Aftaler", "Økonomi", "Planer", "Bilag"]
        for subfolder_name in subfolder_names:
            subfolder_path = os.path.join(folder_path, subfolder_name)
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
        return folder_path

        
class Folder(MPTTModel):
    parent = TreeForeignKey('self', related_name='children', null=True,
                            blank=True, db_index=True,
                            on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    creator = models.ForeignKey(Record, on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

