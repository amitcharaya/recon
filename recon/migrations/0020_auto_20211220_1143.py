# Generated by Django 3.2.9 on 2021-12-20 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recon', '0019_rename_txntpe_transaction_txntype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='id',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='txnNo',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]