from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-input',
        'placeholder': 'your@email.com',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Choose a username',
    }))

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('An account with this email already exists.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_active = False  # Requires admin approval
        user.set_unusable_password()
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Username',
        'autofocus': True,
        'autocomplete': 'off',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-input',
        'placeholder': 'your@email.com',
        'autocomplete': 'off',
    }))

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if username and email:
            try:
                user = User.objects.get(username=username, email__iexact=email)
            except User.DoesNotExist:
                raise forms.ValidationError('No account found with that username and email.')
            if user.is_staff:
                raise forms.ValidationError('Admin accounts must log in at /admin/')
            self.user_cache = user
        return self.cleaned_data

    def get_user(self):
        return self.user_cache
