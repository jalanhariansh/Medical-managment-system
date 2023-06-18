from django import forms
from users.models import Patient
from users.models import User

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['gender', 'phone','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['history_of_illness']
