from django import forms


class Donate(forms.Form):
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1}))
