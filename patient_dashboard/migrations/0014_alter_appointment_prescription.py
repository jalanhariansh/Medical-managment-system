# Generated by Django 4.2.2 on 2023-06-18 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_dashboard', '0013_alter_appointment_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='prescription',
            field=models.ImageField(blank=True, upload_to='prescriptions'),
        ),
    ]
