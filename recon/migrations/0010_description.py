# Generated by Django 3.2.9 on 2021-12-14 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recon', '0009_recondate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256)),
            ],
        ),
    ]
