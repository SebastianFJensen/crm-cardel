# Generated by Django 5.0.1 on 2024-01-23 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_record_kontaktperson_alter_record_lead_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='Postnummer',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='record',
            name='Adresse',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='record',
            name='Lead',
            field=models.CharField(choices=[('Benjamin', 'BENJAMIN'), ('Magnus', 'MAGNUS'), ('Vælg', 'Vælg'), ('Jakob', 'JAKOB'), ('Stefan', 'Stefan'), ('Thomas', 'THOMAS')], default='Vælg', max_length=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='Status',
            field=models.CharField(choices=[('Vælg', 'Vælg'), ('Negotiation', 'NEGOTIATION'), ('Lead', 'LEAD'), ('Lukket aftale', 'LUKKET AFTALE'), ('Lost', 'LOST'), ('Sendt til DLA', 'SENDT TIL DLA')], default='Vælg', max_length=20),
        ),
    ]
