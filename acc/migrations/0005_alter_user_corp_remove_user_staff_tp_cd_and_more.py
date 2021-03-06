# Generated by Django 4.0.1 on 2022-02-14 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_remove_codedt_code_id_codedt_code'),
        ('corp', '0001_initial'),
        ('acc', '0004_remove_user_staff_tp_cd_user_staff_tp_cd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='corp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='corp.corp'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='staff_tp_cd',
        ),
        migrations.AddField(
            model_name='user',
            name='staff_tp_cd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='common.codedt'),
        ),
    ]
