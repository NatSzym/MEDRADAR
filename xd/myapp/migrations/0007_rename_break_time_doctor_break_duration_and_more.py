# Generated by Django 5.0 on 2024-01-12 11:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_patient_email_alter_patient_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='break_time',
            new_name='break_duration',
        ),
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default=datetime.time(12, 0)),
        ),
        migrations.AddField(
            model_name='doctor',
            name='break_start',
            field=models.TimeField(default=datetime.time(12, 0)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default='2015-05-06'),
        ),
    ]