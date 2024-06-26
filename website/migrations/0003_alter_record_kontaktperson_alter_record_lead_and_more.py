# Generated by Django 5.0.1 on 2024-01-23 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_file_file_remove_file_filename_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='Kontaktperson',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='record',
            name='Lead',
            field=models.CharField(choices=[('Magnus', 'MAGNUS'), ('Stefan', 'Stefan'), ('Jakob', 'JAKOB'), ('Benjamin', 'BENJAMIN'), ('Vælg', 'Vælg'), ('Thomas', 'THOMAS')], default='Vælg', max_length=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='Mail',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='record',
            name='Status',
            field=models.CharField(choices=[('Negotiation', 'NEGOTIATION'), ('Lukket aftale', 'LUKKET AFTALE'), ('Sendt til DLA', 'SENDT TIL DLA'), ('Vælg', 'Vælg'), ('Lead', 'LEAD'), ('Lost', 'LOST')], default='Vælg', max_length=20),
        ),
    ]
