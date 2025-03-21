from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0039_tabtstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='opfølgningmaaned',
            field=models.IntegerField(default=0, blank=True, null=True),
        ),
    ]