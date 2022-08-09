from django import forms
from .models import Review_cancion


class NuevaReviewCancion(forms.ModelForm):
   #nota = forms.IntegerField()
   #review = forms.CharField(widget=forms.Textarea()) # <textarea> en vez de <input>

   class Meta:
       model = Review_cancion
       fields = ['nota','comentario']