from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField
)
from .models import User
from django.utils.translation import gettext as _


class LoginForm(AuthenticationForm):
    username = UsernameField(
        label="",
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form form-control',
                'placeholder': 'Email',
            }
        )
    )
    password = forms.CharField(
        label="",
        required=True,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form form-control',
                'placeholder': 'Password',
            }
        )
    )

    class Meta:
        model = User
        exclude = ('', )


class UserRegistrationForm(UserCreationForm):
    """
    username = forms.CharField(
        label="Usuario",
        max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form form-control'})
    )
    """
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form form-control',
                'placeholder': _('Nombre')
            }
        )
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form form-control',
                'placeholder': _('Apellido')
            }
        )
    )
    email = forms.EmailField(
        label="",
        max_length=40,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form form-control',
                'placeholder': 'Email'
            }
        )
    )
    password1 = forms.CharField(
        label="",
        max_length=40,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form form-control',
                'placeholder': _('Contraseña')
            }
        )
    )
    password2 = forms.CharField(
        label="",
        max_length=40,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form form-control',
                'placeholder': _('Confirmar Contraseña')
            }
        )
    )
    is_place_owner = forms.BooleanField(
        label=_("Soy dueño de un lugar"),
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "is_place_owner"
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email)\
                .exclude(email=email).exists():
            raise forms.ValidationError(
                _(u'Ya existe un usuario con este email.')
            )
        return email


class SpotRegistrationForm(UserCreationForm):
    spot_id = forms.IntegerField(
        label="",
        widget=forms.HiddenInput()
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form form-control',
                'placeholder': 'Contact name'
            }
        )
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form form-control',
                'placeholder': 'Contact Last Name'
            }
        )
    )
    email = forms.EmailField(
        label="",
        max_length=40,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form form-control',
                'placeholder': 'Email'
            }
        )
    )
    password1 = forms.CharField(
        label="",
        max_length=40,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form form-control',
                'placeholder': 'Password'
            }
        )
    )
    password2 = forms.CharField(
        label="",
        max_length=40,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form form-control',
                'placeholder': 'Confirm Password'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            "spot_id",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email)\
                .exclude(email=email).exists():
            raise forms.ValidationError(
                u'Ya existe un usuario con este email.'
            )
        return email


class ClubRegistrationForm(UserCreationForm):
    """
    username = forms.CharField(
        label="Usuario",
        max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form form-control'})
    )
    """
    club_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form form-control',
                'required': True,
                'placeholder': 'Name club'
            }
        )
    )
    club_number = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form form-control',
                'required': True,
                'placeholder': 'Número registro club'
            }
        )
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form form-control',
                'placeholder': 'Name contacto'
            }
        )
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form form-control',
                'placeholder': 'Apellido contacto'
            }
        )
    )
    tel = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form form-control',
                'placeholder': 'Teléfono club'
            }
        )
    )
    email = forms.EmailField(
        label="",
        max_length=40,
        required=False,
        widget=forms.EmailInput(
            attrs={
                'class': 'form form-control',
                'placeholder': 'Email'
            }
        )
    )
    password1 = forms.CharField(
        label="",
        max_length=40,
        required=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form form-control',
                'placeholder': 'Password'
            }
        )
    )
    password2 = forms.CharField(
        label="",
        max_length=40,
        required=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form form-control',
                'placeholder': 'Confirm Password'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            "club_name",
            "first_name",
            "last_name",
            "email",
            "tel",
            "password1",
            "password2",
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email)\
                .exclude(email=email).exists():
            raise forms.ValidationError(
                u'Ya existe un usuario con este email.'
            )
        return email
