# Generated by Django 3.2.9 on 2021-12-20 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recon', '0018_alter_rgcs_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='txnTpe',
            new_name='txnType',
        ),
    ]
