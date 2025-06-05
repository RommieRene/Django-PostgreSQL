from django import forms
from .models import Item

INPUT_CLASSES = "w-1/2 py-4 px-6 rounded-xl border bg-white-500 text-black"
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'descroption', 'price', 'image')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,

            }),
            'descroption': forms.Textarea(attrs={
                'class': INPUT_CLASSES,

            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,

            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
            }),

    }
         


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'descroption', 'price', 'image', 'is_sold')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,

            }),
            'descroption': forms.Textarea(attrs={
                'class': INPUT_CLASSES,

            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,

            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
            }),

    }
         