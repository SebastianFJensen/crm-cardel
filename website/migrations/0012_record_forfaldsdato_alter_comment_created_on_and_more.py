# Generated by Django 5.0.1 on 2024-02-09 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_record_lead_alter_record_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='Forfaldsdato',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='Lead',
            field=models.CharField(choices=[('Benjamin', 'BENJAMIN'), ('Magnus', 'MAGNUS'), ('Thomas', 'THOMAS'), ('Jakob', 'JAKOB'), ('Vælg', 'Vælg'), ('Stefan', 'Stefan')], default='Vælg', max_length=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='Status',
            field=models.CharField(choices=[('Sendt til DLA', 'SENDT TIL DLA'), ('Lead', 'LEAD'), ('Lukket aftale', 'LUKKET AFTALE'), ('Vælg', 'Vælg'), ('Lost', 'LOST'), ('Negotiation', 'NEGOTIATION')], default='Vælg', max_length=20),
        ),
    ]
