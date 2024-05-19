from django import forms


class Pythonform(forms.Form):
    name = forms.CharField(min_length=2,max_length=100, required=True)
    email = forms.EmailField()
    age = forms.ImageField()