from django import forms
from .models import Studio

class StudioForm(forms.ModelForm):
    class Meta:
        model = Studio
        fields = '__all__'
        exclude = ('is_active',)