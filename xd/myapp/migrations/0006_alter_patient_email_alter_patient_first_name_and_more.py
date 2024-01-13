# Generated by Django 5.0 on 2024-01-11 12:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(default='xyz@wp.pl', max_length=254, unique=True, validators=[django.core.validators.EmailValidator(message='Enter a valid email address.')], verbose_name='User Email'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='First name should only contain letters.', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Last name should only contain letters.', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pesel',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='PESEL should only contain digits.', regex='^[0-9]*$')]),
        ),
    ]
