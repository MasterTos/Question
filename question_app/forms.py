from django import forms

class PasswordForm(forms.Form):
    password = forms.CharField(max_length=5)