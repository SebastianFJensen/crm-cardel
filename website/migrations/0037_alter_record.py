class Migration(migrations.Migration):

    dependencies = [
        ('website', '0036_record_resights_alter_record_lukket_aftale_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='Bebyggelsesprocent',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='areal_bm2',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='Byggemeterpris',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='Salgssum',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True),
        ),
  ]
