# Generated by Django 4.2.7 on 2025-03-18 15:07

from django.db import migrations, models
from django.contrib.auth.models import User  # Import User model

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0037_record_bebyggelsesprocent_record_byggemeterpris_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_url',
            field=models.URLField(max_length=500),
        ),
        migrations.AddField(
            model_name='file',
            name='uploaded_on',
            field=models.DateTimeField(auto_now_add=False, auto_now=True),
        ),
        migrations.AddField(
            model_name='file',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]