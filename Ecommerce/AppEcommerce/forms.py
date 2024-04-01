from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password')

    def clean_username(self):
        # Get the cleaned username from the form
        username = self.cleaned_data.get('username')

        # Check if a user with the same username already exists
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')

        return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match')
        return cd['password2']
