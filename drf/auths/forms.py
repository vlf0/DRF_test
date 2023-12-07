from django import forms


class UserLogInForm(forms.Form):
    name = forms.CharField(required=False)
    password = forms.CharField(required=False, widget=forms.PasswordInput())


class CategoryCreatingForm(forms.Form):
    name = forms.CharField(max_length=20)


class UserRegistrationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

