# Generated by Django 3.2.9 on 2021-11-23 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=250)),
                ('openingBalance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txnNo', models.CharField(max_length=25)),
                ('drTxn', models.FloatField()),
                ('crTxn', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TxnType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=26)),
            ],
        ),
    ]
