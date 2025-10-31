from django import forms
from .models import FoodItem

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'calories']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Banana', 'class':'w-full rounded-md p-2 border'}),
            'calories': forms.NumberInput(attrs={'placeholder': 'e.g. 105', 'class':'w-full rounded-md p-2 border'}),
        }
