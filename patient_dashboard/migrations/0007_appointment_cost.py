# Generated by Django 4.2.2 on 2023-06-13 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_dashboard', '0006_alter_appointment_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='cost',
            field=models.IntegerField(null=True),
        ),
    ]