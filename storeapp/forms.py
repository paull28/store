from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Form to create/edit a User object, with an additional field for email
class UserCreationWithEmailForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    class Meta:
        model = User
        fields = ("username", "email")

class DeliveryForm(forms.Form):
    fname = forms.CharField(max_length=255)
    lname = forms.CharField(max_length=255)
    postcode = forms.CharField(max_length=8)
    line1 = forms.CharField(max_length=255)
    line2 = forms.CharField(max_length=255, required=False)
    line3 = forms.CharField(max_length=255, required=False)
    phone_number = forms.CharField(max_length=15, required=False)
    country = forms.CharField(max_length=100)
    delivery_instructions = forms.CharField(widget=forms.Textarea, required=False)