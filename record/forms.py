from django import forms
from .models import Position, Area

class PositionForm(forms.ModelForm):
    area_name = forms.CharField(label='Área', required=False, disabled=True)
    company_name = forms.CharField(label='Empresa', required=False, disabled=True)

    class Meta:
        model = Position
        fields = ['name', 'activity_type', 'image', 'public', 'area', 'company_name', 'area_name']

    def __init__(self, *args, **kwargs):
        super(PositionForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.area:
            self.fields['area_name'].initial = self.instance.area.name
            self.fields['company_name'].initial = self.instance.area.company.name

    def clean(self):
        
        cleaned_data = super().clean()
        area = cleaned_data.get('area')

        # Verificar que el área sea obligatoria
        if not area:
            self.add_error('area', 'Por favor, selecciona un área.')

        return cleaned_data
#formulario para agregar Area
class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'description']