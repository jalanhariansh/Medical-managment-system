from django import forms
from patient_dashboard.models import Appointment
from django.views.generic import UpdateView

class AppUpdateForm(UpdateView):
    prescription = forms.ImageField(required = True)
    prescription = forms.IntegerField(required = True)
    model = Appointment
    fields = ['prescription','cost']