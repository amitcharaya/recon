# Generated by Django 3.2.9 on 2021-12-23 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recon', '0029_auto_20211223_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingentries',
            name='adjustmentDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
