# Generated by Django 4.2.2 on 2023-06-12 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=100)),
                ('department', models.CharField(choices=[('ENT', 'ENT'), ('Cardiologist', 'Cardiologist'), ('Neuroologist', 'Neurologist'), ('Oncologist', 'Oncologist'), ('Ortho', 'Ortho')], max_length=15)),
                ('symptoms', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('prescription', models.ImageField(blank=True, upload_to='prescriptions')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]