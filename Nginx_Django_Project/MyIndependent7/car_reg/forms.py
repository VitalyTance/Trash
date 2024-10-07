from django import forms

from .models import Car, Detail, RegDetail
# Create your forms here


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'reg_time': forms.TextInput(attrs={'type': 'datetime-local'})
        }


class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = '__all__'


class RegDetailForm(forms.ModelForm):
    class Meta:
        model = RegDetail
        fields = '__all__'
        widgets = {
            'reg_date': forms.TextInput(attrs={'type': 'datetime-local'})
        }