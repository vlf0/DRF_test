from django import forms


class LogIn(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'display': 'flex'}))
    password = forms.CharField(required=False, widget=forms.PasswordInput)

