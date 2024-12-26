# Generated by Django 5.1.4 on 2024-12-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='email_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reservation',
            name='feedback',
            field=models.TextField(blank=True, null=True),
        ),
    ]
