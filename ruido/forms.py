from django import forms
from .models import RuidoEvaluation


class RuidoEvaluationForm(forms.ModelForm):
    class Meta:
        model = RuidoEvaluation
        exclude = ['position']  # Excluye el campo 'position' del formulario

        
