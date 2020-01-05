from django import forms
from .models import Recipes
from datetime import datetime

class RecipeAddForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = '__all__'
        widgets = {'author_name' : forms.HiddenInput()}


