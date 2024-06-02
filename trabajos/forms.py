#trabajos/forms.py
from django import forms
from .models import TrabajoDeGrado, Modalidad, Actividad


class TrabajoDeGradoForm(forms.ModelForm):
    class Meta:
        model = TrabajoDeGrado
        fields = ['nombre', 'modalidad', 'programa', 'estudiantes', 'jurados', 
                  'asesores', 'profesores', 'empresa', 'fecha_inicio', 'vigente', 'estado', 'actividades']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'modalidad': forms.Select(attrs={'class': 'form-control'}),
            'estudiantes': forms.CheckboxSelectMultiple(),  # Usar SelectMultiple
           
        }    
    
actividades = forms.ModelMultipleChoiceField(
        queryset=Actividad.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
)
    
def __init__(self, *args, **kwargs):
        super(TrabajoDeGradoForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs and kwargs['instance']:
            modalidad = kwargs['instance'].modalidad
            if modalidad:
                self.fields['actividades'].queryset = Actividad.objects.filter(modalidad=modalidad)
                self.fields['actividades'].initial = kwargs['instance'].actividades.all()
        elif 'data' in kwargs and 'modalidad' in kwargs['data']:
            modalidad_id = kwargs['data'].get('modalidad')
            if modalidad_id:
                self.fields['actividades'].queryset = Actividad.objects.filter(modalidad_id=modalidad_id)
        else:
            self.fields['actividades'].queryset = Actividad.objects.none()