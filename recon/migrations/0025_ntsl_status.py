# Generated by Django 3.2.9 on 2021-12-22 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recon', '0024_alter_tipandsurcharge_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='ntsl',
            name='status',
            field=models.CharField(default='Pending', max_length=10),
            preserve_default=False,
        ),
    ]
