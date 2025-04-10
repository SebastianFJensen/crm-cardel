from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0039_record_tabtstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='Kystfredning',
            field=models.CharField(choices=[('Vælg', 'Vælg'), ('Ja', 'Ja'), ('Nej', 'Nej')], default='Vælg', null=True, blank=True, max_length=30),
        ),

        migrations.AddField(
            model_name='record',
            name='Strandbeskyttelse',
            field=models.CharField(choices=[('Vælg', 'Vælg'), ('Ja', 'Ja'), ('Nej', 'Nej')], default='Vælg', null=True, blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='record',
            name='Projekttype',
            field=models.CharField(choices=[('Almindeligt', 'Almindeligt'), ('Sommerhuse', 'Sommerhuse')], default='Almindeligt', null=True, blank=True, max_length=30),
        ),
        ]