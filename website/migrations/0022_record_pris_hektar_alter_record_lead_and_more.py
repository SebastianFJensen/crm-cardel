# Generated by Django 5.0.1 on 2024-02-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_alter_record_lead_alter_record_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='Pris_Hektar',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='Lead',
            field=models.CharField(choices=[('Jakob', 'JAKOB'), ('Magnus', 'MAGNUS'), ('Stefan', 'Stefan'), ('Vælg', 'Vælg'), ('Benjamin', 'BENJAMIN'), ('Thomas', 'THOMAS')], default='Vælg', max_length=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='Status',
            field=models.CharField(choices=[('Negotiation', 'NEGOTIATION'), ('Lukket aftale', 'LUKKET AFTALE'), ('Lost', 'LOST'), ('Lead', 'LEAD'), ('Vælg', 'Vælg'), ('Sendt til DLA', 'SENDT TIL DLA')], default='Vælg', max_length=20),
        ),
    ]
