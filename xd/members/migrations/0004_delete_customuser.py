# Generated by Django 5.0 on 2024-01-10 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_customuser_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]