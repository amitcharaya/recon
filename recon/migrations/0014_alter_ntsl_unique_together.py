# Generated by Django 3.2.9 on 2021-12-16 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recon', '0013_alter_ntsl_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ntsl',
            unique_together={('date', 'cycle', 'description')},
        ),
    ]
