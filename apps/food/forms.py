from django import forms 

from .models import Food_Channel 


class FoodChanneForm(forms.ModelForm):

    class Meta:
        model = Food_Channel
        fields = '__all__'

