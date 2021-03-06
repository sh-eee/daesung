# Generated by Django 4.0.1 on 2022-02-14 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_remove_codedt_code_id_codedt_code'),
        ('client', '0002_remove_client_biz_tp_cd_client_biz_tp_cd_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='biz_tp_cd',
        ),
        migrations.AddField(
            model_name='client',
            name='biz_tp_cd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='biz_type', to='common.codedt'),
        ),
        migrations.RemoveField(
            model_name='client',
            name='client_tp_cd',
        ),
        migrations.AddField(
            model_name='client',
            name='client_tp_cd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_type', to='common.codedt'),
        ),
    ]
