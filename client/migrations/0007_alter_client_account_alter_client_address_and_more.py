# Generated by Django 4.0.1 on 2022-02-18 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_remove_client_biz_tp_cd_remove_client_client_tp_cd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='account',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='address2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='bank',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='cellphone',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='corp_nm',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='corp_no',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='telephone',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='zipcode',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
