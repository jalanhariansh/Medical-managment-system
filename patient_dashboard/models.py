from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.

DEPARTMENTS = (
    ('ENT', 'ENT'), 
    ('Cardiologist', 'Cardiologist'), 
    ('Neurologist', 'Neurologist'), 
    ('Oncologist', 'Oncologist'), 
    ('Ortho', 'Ortho')
)
class Appointment(models.Model):
    doc_name = models.CharField('Doc preffered(if any)',blank=True,default="", max_length=100)
    department = models.CharField(choices=DEPARTMENTS,max_length=15)
    symptoms = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    prescription = models.ImageField(blank=True, upload_to='prescriptions')
    cost = models.IntegerField(null=True)
    patient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('home')