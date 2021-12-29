from django import forms


class UserRegistrationForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField()
	first_name = forms.CharField()
	last_name = forms.CharField()


class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()
