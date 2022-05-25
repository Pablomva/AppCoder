from django import forms

class FormProductor(forms.Form):
    nombre=forms.CharField(max_length=255)
    apellido=forms.CharField(max_length=255)
    email=forms.EmailField()
    provincia=forms.CharField(max_length=255)
    descripcion=forms.CharField(widget=forms.Textarea)
    cultivo=forms.CharField(max_length=255)