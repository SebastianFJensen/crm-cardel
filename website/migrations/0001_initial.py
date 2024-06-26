# Generated by Django 5.0.1 on 2024-01-16 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foldername', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('BFE_Nummer', models.CharField(max_length=20)),
                ('Adresse', models.CharField(max_length=20)),
                ('Kommune', models.CharField(max_length=20)),
                ('Region', models.CharField(max_length=20)),
                ('Kontaktperson', models.CharField(max_length=20)),
                ('Mail', models.CharField(max_length=20)),
                ('Telefonnummer', models.CharField(max_length=20)),
                ('m2', models.CharField(max_length=20)),
                ('Kommuneplan', models.CharField(max_length=20)),
                ('Lokalplan', models.CharField(max_length=20)),
                ('Formål', models.CharField(max_length=20)),
                ('Sendt_til_DLA', models.BooleanField(default=False)),
                ('Lead', models.CharField(choices=[('Jakob', 'JAKOB'), ('Stefan', 'Stefan'), ('Vælg', 'Vælg'), ('Thomas', 'THOMAS'), ('Magnus', 'MAGNUS'), ('Benjamin', 'BENJAMIN')], default='Vælg', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='Files')),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.folder')),
            ],
        ),
        migrations.AddField(
            model_name='folder',
            name='folderuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.record'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='website.record')),
            ],
        ),
    ]
