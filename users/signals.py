from django.db.models.signals import post_save
from allauth.socialaccount.models import SocialAccount
from .models import Patient

def create_profile(sender, instance, created, **kwargs):
   if created:
      instance.user.is_patient = True
      instance.user.save()
      Patient.objects.create(user=instance.user)

def save_profile(sender, instance, **kwargs):
    instance.user.patient.save()

post_save.connect(create_profile, sender=SocialAccount)
post_save.connect(save_profile, sender=SocialAccount)
