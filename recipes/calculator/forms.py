from django import forms


class MyForm(forms.Form):
    number = forms.IntegerField()
    