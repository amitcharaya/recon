# Generated by Django 3.2.9 on 2021-12-16 07:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recon', '0015_channel_inwardoutward_rgcs_status_transactioncycle_transactiontype'),
    ]

    operations = [
        migrations.AddField(
            model_name='rgcs',
            name='cycle',
            field=models.CharField(default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
    ]