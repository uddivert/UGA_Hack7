from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(empty_value="Email")
    password = forms.CharField(max_length=50, empty_value="password")