from django import forms

from .models import Character

class PostForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = ('name', 'race', 'cclass',)