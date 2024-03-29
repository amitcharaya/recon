# Generated by Django 3.2.9 on 2021-12-16 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recon', '0014_alter_ntsl_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='InwardOutward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionCycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactionCycle', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactionType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RGCS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('productName', models.CharField(max_length=50)),
                ('bankName', models.CharField(max_length=250)),
                ('settlementBin', models.CharField(max_length=50)),
                ('acqId', models.CharField(max_length=50)),
                ('txnCount', models.IntegerField()),
                ('txnCCY', models.IntegerField()),
                ('txnAmtDr', models.FloatField()),
                ('txnAmtCr', models.FloatField()),
                ('setCCY', models.IntegerField()),
                ('setAmtDr', models.FloatField()),
                ('setAmtCr', models.FloatField()),
                ('intFeeAmtDr', models.FloatField()),
                ('intFeeAmtCr', models.FloatField()),
                ('memIncFeeAmtDr', models.FloatField()),
                ('memIncFeeAmtCr', models.FloatField()),
                ('customerCompensationDr', models.FloatField()),
                ('customerCompensationCr', models.FloatField()),
                ('othFeeAmtDr', models.FloatField()),
                ('othFeeAmtCr', models.FloatField()),
                ('othFeeGstDr', models.FloatField()),
                ('othFeeGstCr', models.FloatField()),
                ('finalSumCr', models.FloatField()),
                ('finalSumDr', models.FloatField()),
                ('finalNet', models.FloatField()),
                ('channel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recon.channel')),
                ('inwardOutward', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recon.inwardoutward')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recon.status')),
                ('transactionCycle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recon.transactioncycle')),
                ('transactionType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recon.transactiontype')),
            ],
        ),
    ]
