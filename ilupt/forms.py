from django import forms
from .models import LightingEvaluation

class LightingEvaluationForm(forms.ModelForm):
    class Meta:
        model = LightingEvaluation
        fields = '__all__'  # Esto incluirá todos los campos de tu modelo en el formulario
        widgets = {
            'average': forms.NumberInput(attrs={'id': 'average'}),
            'maximum': forms.NumberInput(attrs={'id': 'maximum'}),
            'minimum': forms.NumberInput(attrs={'id': 'minimum'}),
            'left_1': forms.NumberInput(attrs={'id': 'left_1'}),
            'left_2': forms.NumberInput(attrs={'id': 'left_2'}),
            'left_3': forms.NumberInput(attrs={'id': 'left_3'}),
            'left_4': forms.NumberInput(attrs={'id': 'left_4'}),
            'left_5': forms.NumberInput(attrs={'id': 'left_5'}),
            'center_1': forms.NumberInput(attrs={'id': 'center_1'}),
            'center_2': forms.NumberInput(attrs={'id': 'center_2'}),
            'center_3': forms.NumberInput(attrs={'id': 'center_3'}),
            'center_4': forms.NumberInput(attrs={'id': 'center_4'}),
            'center_5': forms.NumberInput(attrs={'id': 'center_5'}),
            'right_1': forms.NumberInput(attrs={'id': 'right_1'}),
            'right_2': forms.NumberInput(attrs={'id': 'right_2'}),
            'right_3': forms.NumberInput(attrs={'id': 'right_3'}),
            'right_4': forms.NumberInput(attrs={'id': 'right_4'}),
            'right_5': forms.NumberInput(attrs={'id': 'right_5'}),
            # define los widgets para los demás campos si es necesario
        }
