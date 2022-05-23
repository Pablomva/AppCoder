from django import forms

class FormularioProductor(forms.Form):
    cultivo=forms.CharField()
    provincia=forms.CharField()
