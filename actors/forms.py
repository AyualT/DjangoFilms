from django import forms
from .models import Actor

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'
        exclude = ('is_active',)