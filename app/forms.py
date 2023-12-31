from django import forms
from .models import *

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'

class RecetaPDFForm(forms.ModelForm):
    class Meta:
        model = RecetaPDF
        fields = ['pdf_file']