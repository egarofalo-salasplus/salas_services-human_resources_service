from django import forms

class ImputationForm(forms.Form):
    board = forms.ChoiceField(choices=[], label="Selecciona un tablero")
    email = forms.EmailField(label="Correo electrónico a imputar")