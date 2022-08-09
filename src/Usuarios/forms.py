from django import forms
from django.contrib.auth import authenticate
from django.core.validators import MaxLengthValidator, RegexValidator, slug_re, EmailValidator
from Usuarios.models import User


class LoginForm(forms.Form):
    user = forms.CharField(
        label='Nombre de Usuario',
        required=True,
        validators=[
            MaxLengthValidator(
                20, "El nombre de usuario ingresado supera el largo maximo."),
            RegexValidator(
                slug_re, "El nombre de usuario solo puede consistir en letras, numeros, guiones y guiones bajo."),
        ]
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(),
        required=True,
        validators=[
            MaxLengthValidator(
                20, "La contraseña ingresado supera el largo maximo."),
            RegexValidator(
                slug_re, "La contraseña solo puede consistir en letras, numeros, guiones y guiones bajo."),
        ]
    )

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get("user")
        password = cleaned_data.get("password")
        if not authenticate(username=user, password=password):
            msg = "La contraseña y el nombre de usuario no coinciden."
            self.add_error('user', msg)
            self.add_error('password', msg)


class RegisterForm(forms.Form):
    user = forms.CharField(
        label='Nombre de Usuario',
        required=True,
        validators=[
            MaxLengthValidator(
                20, "El nombre de usuario ingresado supera el largo maximo."),
            RegexValidator(
                slug_re, "El nombre de usuario solo puede consistir en letras, numeros, guiones y guiones bajo."),
        ],
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese su nombre de usuario..."})
    )
    email = forms.EmailField(label="Email",
                             widget=forms.EmailInput(
                                 attrs={"placeholder": "Ingrese su email..."}),
                             required=True)
    pronombres = forms.ChoiceField(
        choices=[('La', 'La'), ('El', 'El'), ('Le', 'Le'), ('Otro', 'Otro')])
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={"placeholder": "Ingrese su contraseña..."}),
        required=True,
        validators=[
            MaxLengthValidator(
                20, "La contraseña ingresada supera el largo maximo."),
            RegexValidator(
                slug_re, "La contraseña solo puede consistir en letras, numeros, guiones y guiones bajo."),
        ],
    )

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get("user")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if User.objects.filter(username=user).exists():
            self.add_error('user', "El nombre de usuario escogido ya existe")

        if User.objects.filter(username=email).exists():
            self.add_error('user', "El email ingresado ya tiene una cuenta")


class ChangePasswordForm(forms.Form):
    user = forms.CharField(
        label='Nombre de Usuario',
        required=True,
        validators=[
            MaxLengthValidator(
                20, "El nombre de usuario ingresado supera el largo maximo."),
            RegexValidator(
                slug_re, "El nombre de usuario solo puede consistir en letras, numeros, guiones y guiones bajo."),
        ],
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese su nombre de usuario..."})
    )
    email = forms.EmailField(label="Email",
                             widget=forms.EmailInput(
                                 attrs={"placeholder": "Ingrese su email..."}),
                             required=True)

    new_password = forms.CharField(
        label='Nueva contraseña',
        widget=forms.PasswordInput(
            attrs={"placeholder": "Ingrese su nueva contraseña..."}),
        required=True,
        validators=[
            MaxLengthValidator(
                20, "La contraseña ingresada supera el largo maximo."),
            RegexValidator(
                slug_re, "La contraseña solo puede consistir en letras, numeros, guiones y guiones bajo."),
        ],
    )

    confirm_password = forms.CharField(
        label='Confirmar nueva contraseña',
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirme su nueva contraseña..."}),
        required=True,
        validators=[
            MaxLengthValidator(
                20, "La contraseña ingresada supera el largo maximo."),
            RegexValidator(
                slug_re, "La contraseña solo puede consistir en letras, numeros, guiones y guiones bajo."),
        ],
    )

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get("user")
        email = cleaned_data.get("email")
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if not new_password == confirm_password:
            msg = "Las contraseñas no coinciden"
            self.add_error('new_password', msg)
            self.add_error('confirm_password', msg)

        elif User.objects.filter(username=user).get().correo != email:
            self.add_error(
                'email', "El correo ingresado no corresponde a la cuenta")
