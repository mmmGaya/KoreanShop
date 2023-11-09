from django import forms

QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class AddToBasketForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int, label='ш.т.')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    