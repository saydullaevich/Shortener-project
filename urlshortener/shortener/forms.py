
from django import forms

from .models import Shortener

class ShortenerForm(forms.ModelForm):
    
    url_first = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Qisqartirish uchun URL manzilingiz"}))
    
    class Meta:
        model = Shortener

        fields = ('url_first',)