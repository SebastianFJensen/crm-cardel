from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from import_export import resources
from django.db.models.signals import post_save
from django.utils import timezone
import uuid
import os
import unicodedata
from datetime import datetime
from dateutil.relativedelta import relativedelta


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
    Aftale = [
        ('Vælg', 'Vælg'),
        ('Option forlænges', 'OPTION FORLÆNGES'),
        ('Forhandlinger HoT', 'FORHANDLINGER HoT'),
        ('Forhandlinger SPA', 'FORHANDLINGER SPA'),
        ('Underskrevet HoT', 'UNDERSKREVET HoT'),
        ('Underskrevet SPA', 'UNDERSKREVET SPA'), 
        ('Lukket sag', 'LUKKET SAG'),
    ]
    Mstatus = [
    ('Møde booket', 'Møde booket'),
    ('Ombook', 'Ombook'),
    ('Møde aflyst', 'Møde aflyst'),
    ]
    Lstatus = [
        ('VÆLG', 'Vælg'),
        ('PRIS', 'Pris'),
        ('INGEN INTERESSE', 'ingen interesse'),
        ('ANDEN UDVIKLER', 'Anden Udvikler'),
        ('TABT OPTION', 'Tabt option'),
    ]
    Kfredning = [
        ("Vælg", "Vælg"),
        ("Ja", "Ja"),
        ("Nej", "Nej"),
    ]

    Sbeskyttelse = [
        ("Vælg", "Vælg"),
        ("Ja", "Ja"),
        ("Nej", "Nej"),
    ]

    Projekttyper = [
        ("Almindeligt", "Almindeligt"), 
        ("Sommerhuse", "Sommerhuse"),
    ]
    
    created_at = models.DateTimeField(auto_now_add=True)
    BFE_Nummer = models.CharField(max_length=20, null=True)
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
    Lukket_aftale_Status = models.CharField(max_length=30, choices=Aftale, default='Vælg', null=True, blank=True)
    Moedestatus = models.CharField(max_length=30, choices=Mstatus, null=True, blank=True)
    Lead = models.CharField(max_length=10, choices=Ansvarlig, default='Vælg')
    Forfaldsdato = models.DateField(null=True, blank=True)
    Opfølgningsdato = models.DateField(null=True, blank=True)
    Resights = models.URLField(max_length=200, blank=True)
    Bebyggelsesprocent = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    areal_bm2 = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    Byggemeterpris = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    Salgssum = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    Tabtstatus = models.CharField(max_length=30, choices=Lstatus, null=True, blank=True)
    opfølgningmaaned = models.IntegerField(default=0, blank=True, null=True)
    Kystfredning = models.CharField(max_length=10, choices=Kfredning, default='Vælg', null=True, blank=True)
    Strandbeskyttelse = models.CharField(max_length=10, choices=Sbeskyttelse, default='Vælg', null=True, blank=True)
    Projekttype = models.CharField(max_length=25, choices=Projekttyper, default='Almindeligt')


    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return(f"{self.BFE_Nummer}")
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.areal_bm2 is None:
            self.areal_bm2 = ''
        if self.m2 is None:
            self.m2 = ''

    def save(self, *args, **kwargs):
        # Calculate opfølgningmaaned based on Tabtstatus
        if self.Tabtstatus:
            months_mapping = {
                'PRIS': 6,
                'INGEN INTERESSE': 12,
                'ANDEN UDVIKLER': 12,
                'TABT OPTION': 12,
            }
            # Get the number of months based on the current Tabtstatus
            self.opfølgningmaaned = months_mapping.get(self.Tabtstatus, 0)

            # Calculate the new Opfølgningsdato based on the current date
            if self.opfølgningmaaned > 0:
                self.Opfølgningsdato = timezone.now().date() + relativedelta(months=self.opfølgningmaaned)

        # Always recalculate opfølgningmaaned based on Opfølgningsdato
        if self.Opfølgningsdato:
            # Calculate the number of months from now to Opfølgningsdato
            months_difference = (self.Opfølgningsdato - timezone.now().date()).days // 30
            self.opfølgningmaaned = months_difference  # Allow negative values if overdue

        # Call the original save method
        super().save(*args, **kwargs)


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
    file_url = models.URLField(max_length=500)
    uploaded_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.files}"
