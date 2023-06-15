from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(null=True, unique=True)
    phone = PhoneNumberField(null=True, blank=False, unique=True)
    gender = models.CharField(null=True, max_length=1, choices=(('M','Male'),('F','Female')))
    is_patient = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='patient')
    history_of_illness = models.TextField()
