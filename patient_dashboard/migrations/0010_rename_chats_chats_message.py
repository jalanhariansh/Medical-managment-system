# Generated by Django 4.2.2 on 2023-06-17 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient_dashboard', '0009_alter_chats_chats'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chats',
            old_name='chats',
            new_name='message',
        ),
    ]
