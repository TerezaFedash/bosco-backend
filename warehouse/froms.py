from django import forms

class ProductForms(forms.Form):
    name = forms.CharField(max_length=48)
    material = forms.CharField(max_length=48)
    dimensions = forms.CharField(max_length=48)
    color = forms.CharField(max_length=48)
    price = forms.CharField(max_length=48)