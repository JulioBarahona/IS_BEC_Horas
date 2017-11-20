from django import forms
from home.models import Actividad

class HomeForm(forms.ModelForm):
    post = forms.CharField()
    canthoras= forms.IntegerField()
    fecha = forms.DateField()
    descripcion= forms.CharField()

    class Meta:
        model = Actividad
        fields = (
        'post',
        'canthoras',
        'fecha',
        'descripcion',
        )
