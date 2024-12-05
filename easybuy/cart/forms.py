from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        max_value=100,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 1,  # Limite mínimo
            'max': 100,  # Limite máximo
            'oninput': "this.value = Math.min(Math.max(this.value, 1), 100)"  # Validación en tiempo real
        })
    )
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
