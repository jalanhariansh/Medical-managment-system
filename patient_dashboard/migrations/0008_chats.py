# Generated by Django 4.2.2 on 2023-06-17 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_dashboard', '0007_appointment_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.TextField()),
                ('chats', models.TextField()),
            ],
        ),
    ]
