from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0038_file_file_url_file_uploaded_on_file_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='tabtstatus',
            field=models.CharField(choices=[('VÆLG', 'Vælg'), ('PRIS', 'Pris'), ('INGEN INTERESSE', 'ingen interesse'), ('ANDEN UDVIKLER', 'Anden Udvikler'), ('TABT OPTION', 'Tabt option')], null=True, blank=True, max_length=30),
        ),
    ]