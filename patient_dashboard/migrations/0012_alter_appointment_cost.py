# Generated by Django 4.2.2 on 2023-06-17 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_dashboard', '0011_alter_chats_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='cost',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
