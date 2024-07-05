from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from .models import Medicine


class PatientForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    place = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    def clean(self):
        data =  super().clean()
        ph = data.get('phone')
        if len(str(ph)) != 10:
          raise ValidationError("phone number must be 10 digit", "phone")
          
        return data
    
class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields ="__all__"
     