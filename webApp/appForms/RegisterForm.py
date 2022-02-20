from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    phone_number = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    street_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Street Name'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'City'}))
    zip_code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Zip Code'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': "UserName"}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))






