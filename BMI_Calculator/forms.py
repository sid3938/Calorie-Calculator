from django import forms
from .models import Bmi

class BmiForm(forms.ModelForm):
    class Meta:
        model = Bmi
        fields = ["weight", "height"]
        widgets = {
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your weight in kg'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your height in cm'}),
            # 'bmi': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
