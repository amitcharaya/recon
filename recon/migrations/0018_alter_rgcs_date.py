# Generated by Django 3.2.9 on 2021-12-16 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recon', '0017_auto_20211216_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rgcs',
            name='date',
            field=models.DateField(null=True),
        ),
    ]