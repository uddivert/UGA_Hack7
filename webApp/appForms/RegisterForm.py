from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    '''phone = forms.CharField(label='phone, max_length=10')
    address = forms.CharField(label='address')
    email = forms.EmailField()
    password = forms.PasswordInput()'''






