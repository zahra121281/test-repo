# Generated by Django 5.0.3 on 2024-12-11 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counseling', '0002_psychiatrist_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='psychiatrist',
            name='clinic_address',
        ),
        migrations.RemoveField(
            model_name='psychiatrist',
            name='clinic_telephone_number',
        ),
        migrations.RemoveField(
            model_name='psychiatrist',
            name='description',
        ),
    ]
