from django import forms
from .models import Review_pelicula


class FiltrosPelicula(forms.ModelForm):
    # Permite hacer filtros y redirigue a pagnia 0 de listado pelis con los filtros aplicados
    pass


class NuevaReviewPelicula(forms.ModelForm):
    #nota = forms.IntegerField()
    # review = forms.CharField(widget=forms.Textarea()) # <textarea> en vez de <input>

    class Meta:
        model = Review_pelicula
        fields = ['nota', 'comentario']
