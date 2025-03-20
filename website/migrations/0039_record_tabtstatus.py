from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0038_file_file_url_file_uploaded_on_file_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='Tabtstatus',
            field=models.CharField(max_length=30, choices=Lstatus, null=True, blank=True),
        ),
    ]