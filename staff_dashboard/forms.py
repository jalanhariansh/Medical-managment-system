from django import forms
from patient_dashboard.models import Appointment
from django.views.generic import UpdateView
from django import forms

class AppUpdateForm(forms.ModelForm):
    prescription = forms.ImageField(required=True)
    class Meta:
        model = Appointment
        fields = ['prescription','cost']