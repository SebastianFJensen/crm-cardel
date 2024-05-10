from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from import_export import resources
from django.db.models.signals import post_save
import uuid
import os
import unicodedata
from datetime import datetime


class Record(models.Model):
    Ansvarlig = [
        ('Vælg', 'Vælg'),
        ('Benjamin', 'BENJAMIN'),
        ('Jacob', 'JACOB'),
        ('Magnus', 'MAGNUS'),
        ('Martine', 'MARTINE'),
        ('Stefan', 'STEFAN'),
        ('Thomas', 'THOMAS'),
    ]
    Typen = [
        ('Vælg', 'Vælg'),
        ('Lead', 'LEAD'),
        ('Kontakt etableret', 'KONTAKT ETABLERET'),
        ('Møde booket', 'MØDE BOOKET'),
        ('Møde afholdt', 'MØDE AFHOLDT'),
        ('Bud sendt', 'BUD SENDT'),
        ('Forhandling bud', 'FORHANDLING BUD'),
        ('Afventer DLA', 'AFVENTER DLA'),
        ('Forhandling option', 'FORHANDLING OPTION'),
        ('Afventer underskrift', 'AFVENTER UNDERSKRIFT'),
        ('Lukket aftale', 'LUKKET AFTALE'),
        ('Lost', 'LOST'),
    ]
    Lukket_aftale_Status = [
        ('Vælg', 'Vælg'),
        ('Option forlænges', 'OPTION FORLÆNGES'),
        ('Forhandlinger HoT', 'FORHANDLINGER HoT'),
        ('Forhandlinger SPA', 'FORHANDLINGER SPA'),
        ('Underskrevet HoT', 'UNDERSKREVET HoT'),
        ('Underskrevet SPA', 'UNDERSKREVET SPA'), 
        ('Lukket sag', 'LUKKET SAG'),
    ]
    Moedestatus = [
    ('Møde booket', 'Møde booket'),
    ('Ombook', 'Ombook'),
    ('Møde aflyst', 'Møde aflyst'),
    ]
    created_at = models.DateTimeField(auto_now_add=True)
    BFE_Nummer = models.CharField(max_length=20, null=True, unique=True)
    Adresse = models.CharField(max_length=60, null=True)
    Postnummer = models.CharField(max_length=4, null=True)
    By = models.CharField(max_length=80, blank=True)
    Kommune = models.CharField(max_length=20, null=True)
    Region = models.CharField(max_length=20, null=True)
    Kontaktperson = models.CharField(max_length=60, null=True)
    Mail = models.CharField(max_length=60, blank=True, null=True)
    Telefonnummer = models.CharField(max_length=20, blank=True, null=True)
    m2 = models.CharField(max_length=20, null=True, blank=True)
    Kommuneplan = models.CharField(max_length=20, null=True, blank=True)
    Lokalplan = models.CharField(max_length=20, null=True, blank=True)
    Formaal = models.CharField(max_length=50, null=True, blank=True)
    Status = models.CharField(max_length=25, choices=Typen, default='Vælg')
    Lukket_aftale_Status = models.CharField(max_length=30, choices=Lukket_aftale_Status, default='Vælg', null=True, blank=True)
    Moedestatus = models.CharField(max_length=30, choices=Moedestatus, null=True, blank=True)
    Lead = models.CharField(max_length=10, choices=Ansvarlig, default='Vælg')
    Forfaldsdato = models.DateField(null=True, blank=True)
    Opfølgningsdato = models.DateField(null=True, blank=True)
    Resights = models.URLField(max_length=200, blank=True)
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return(f"{self.BFE_Nummer}")


class Comment(models.Model):
    post = models.ForeignKey(Record, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return f"{self.post.BFE_Nummer}"

class RecordResource(resources.ModelResource):
    class Meta:
        model = Record
        import_id_fields = ["BFE_Nummer"]
        skip_unchanged = True
        use_bulk = True

def get_file_location(instance, filename):
    if instance.folder is None:
        raise ValueError("Folder must be set before saving the file")

    upload_date = datetime.now().strftime('%Y%m%d')
    filename_parts = os.path.splitext(filename)
    filename_base = unicodedata.normalize('NFKD', filename_parts[0]).encode('ascii', 'ignore').decode()
    filename_ext = filename_parts[1]
    return f"{instance.folder.record.id}/{instance.folder.folder_type}/{filename_base}{filename_ext}"

class Folder(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='folders')
    name = models.CharField(max_length=180)
    folder_type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.record.id} - {self.folder_type}"

@receiver(post_save, sender=Record)
def create_folder(sender, instance, created, **kwargs):
    if created:
        folder_types = ['Aftaler', 'Økonomi', 'Planer', 'Bilag']
        for folder_type in folder_types:
            Folder.objects.create(record=instance, name=folder_type, folder_type=folder_type)

class File(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, related_name='allfiles')
    files = models.FileField(upload_to=get_file_location, max_length=500)

    def __str__(self):
        return f"{self.files}"
