from django import forms
from django.forms import ModelForm, TextInput, EmailInput,PasswordInput,NumberInput

from .models import Users, Products

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'lastname', 'phone', 'id', 'email', 'password']
        
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class':'label',
        'style':'width: 200px;height: 20px;border-radius: 0.3vw 0.3vw 0.3vw 0.3vw;border-style: groove;border-width: .1vw;border-color: black;'
        }))
    lastname = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class':'label',
        'style':'width: 200px;height: 20px;border-radius: 0.3vw 0.3vw 0.3vw 0.3vw;border-style: groove;border-width: .1vw;border-color: black;'
        }))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'label',
        'style':'width: 200px;height: 20px;border-radius: 0.3vw 0.3vw 0.3vw 0.3vw;border-style: groove;border-width: .1vw;border-color: black;'
        }))
    id = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'label',
        'style':'width: 200px;height: 20px;border-radius: 0.3vw 0.3vw 0.3vw 0.3vw;border-style: groove;border-width: .1vw;border-color: black;'
        }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'label',
        'style':'width: 200px;height: 20px;border-radius: 0.3vw 0.3vw 0.3vw 0.3vw;border-style: groove;border-width: .1vw;border-color: black;'
        }))
    password = forms.CharField(max_length=400,widget=forms.PasswordInput(attrs={
        'class':'label',
        'style':'width: 200px;height: 20px;border-radius: 0.3vw 0.3vw 0.3vw 0.3vw;border-style: groove;border-width: .1vw;border-color: black;'
        }))

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['amount', 'cart']
    
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'label',
        'style':'width: 240px;height: 35px; border-radius: 0.3vw 0vw 0vw 0.3vw; border-style: solid;border-width: .1vw;border-color: grey; margin-right: -5px; margin-top: -1px;',
        'placeholder':'AMOUNT'
        }), min_value=1, required=True)
        
    cart = forms.BooleanField(widget=forms.widgets.CheckboxInput(attrs={
        'class':'label'
        }), required=False, disabled=False, initial=True)
    