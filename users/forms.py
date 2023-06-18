from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'phone','gender','first_name','last_name','password1', 'password2']
    
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
        return user