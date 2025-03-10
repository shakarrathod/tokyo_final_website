# Generated by Django 5.1.5 on 2025-02-05 07:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_enquiry_email_alter_enquiry_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='source_page',
            field=models.CharField(default='Unknown', max_length=20),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='phone',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid 10-digit Indian phone number.', regex='^[6-9]\\d{9}$')]),
        ),
    ]
