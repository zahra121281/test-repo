# Generated by Django 5.0.3 on 2024-12-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctorpanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freetime',
            name='time',
            field=models.TimeField(choices=[('00:00:00', '00:00:00'), ('01:00:00', '01:00:00'), ('02:00:00', '02:00:00'), ('03:00:00', '03:00:00'), ('04:00:00', '04:00:00'), ('05:00:00', '05:00:00'), ('06:00:00', '06:00:00'), ('07:00:00', '07:00:00'), ('08:00:00', '08:00:00'), ('09:00:00', '09:00:00'), ('10:00:00', '10:00:00'), ('11:00:00', '11:00:00'), ('12:00:00', '12:00:00'), ('13:00:00', '13:00:00'), ('14:00:00', '14:00:00'), ('15:00:00', '15:00:00'), ('16:00:00', '16:00:00'), ('17:00:00', '17:00:00'), ('18:00:00', '18:00:00'), ('19:00:00', '19:00:00'), ('20:00:00', '20:00:00'), ('21:00:00', '21:00:00'), ('22:00:00', '22:00:00'), ('23:00:00', '23:00:00')], null=True),
        ),
    ]
