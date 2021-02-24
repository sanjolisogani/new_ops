from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from .models import *
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=254,required=True)

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'email', 'password1', 'password2', )
        #fields = '__all__'

class CustomEmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email_id = self.cleaned_data['email']
        if not Users.objects.filter(email__iexact=email_id).exists():
            raise ValidationError("Email invalid!")
            
            print("invalid email")

        return email_id