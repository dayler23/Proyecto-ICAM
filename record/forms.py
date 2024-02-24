from django import forms
from .models import Position, Area

class PositionForm(forms.ModelForm):
    

    class Meta:
        model = Position
        fields = ['name', 'activity_type', 'image', 'public']

    

#formulario para agregar Area
class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'description']