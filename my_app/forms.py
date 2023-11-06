from django import forms
from .models import PaymentDeets
from django.forms import ModelForm, TextInput, EmailInput,PasswordInput,NumberInput

class PaymentForm(ModelForm):
    class Meta:
        model = PaymentDeets
        fields = ['phone_no', 'amount']
    
    phone_no = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'',
        'style':'width: 200px;height: 20px;border-radius: 0.3vw 0.3vw 0.3vw 0.3vw;border-style: groove;border-width: .1vw;border-color: black;',
        'value':'0716551972'
        }), required=False, )
    
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'',
        'style':'width: 200px;height: 19px;border-radius: 0.3vw 0.3vw 0.3vw 0.3vw;border-style: groove;border-width: .1vw;border-color: black;'
        }))
