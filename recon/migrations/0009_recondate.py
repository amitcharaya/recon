# Generated by Django 3.2.9 on 2021-12-13 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recon', '0008_auto_20211202_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReconDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
    ]