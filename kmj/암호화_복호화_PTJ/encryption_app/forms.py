from django import forms
from .models import Encryption,Decryption

class EncryptionForm(forms.ModelForm):
    class Meta:
        model = Encryption
        fields = ('content','key')

class DecryptionForm(forms.ModelForm):
    class Meta:
        model = Decryption
        fields = ('content','key')