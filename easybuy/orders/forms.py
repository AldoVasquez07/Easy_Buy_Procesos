from django import forms
from .models import Order
from django.core.exceptions import ValidationError
import re

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email']

    # Validación para `first_name`
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', first_name):
            raise ValidationError("First name can only contain letters and spaces.")
        return first_name

    # Validación para `last_name`
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', last_name):
            raise ValidationError("Last name can only contain letters and spaces.")
        return last_name

    # Validación para `email`
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Usa la validación de correo integrada
        if not forms.EmailField().clean(email):
            raise ValidationError("Please enter a valid email address.")
        return email
