from django.forms import ModelForm
from django import forms

from NIP_checker_app.models import NIP


class NIPForm(ModelForm):
    class Meta:
        model = NIP
        fields = ['nip_number']




class Login4Form(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)
