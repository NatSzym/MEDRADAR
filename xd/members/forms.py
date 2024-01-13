from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import EmailValidator, RegexValidator


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             validators=[EmailValidator(message='Enter a valid email address.')])
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                validators=[RegexValidator(regex='^[a-zA-Z]*$',
                                                         message='First name should only contain letters.')])
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}),
                               validators=[RegexValidator(regex='^[a-zA-Z]*$',
                                                        message='Last name should only contain letters.')])

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
