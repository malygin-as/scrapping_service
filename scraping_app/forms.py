from django import forms
from .models import City, CodeLang


class SearchForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        to_field_name='slug',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Город',
        )
    codelang = forms.ModelChoiceField(
        queryset=CodeLang.objects.all(),
        to_field_name='slug',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Язык программирования'
        )
