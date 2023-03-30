from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control form-control-user",
                                                     'placeholder': "Email Address"}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control form-control-user',
                                                                              'id': 'exampleFirstName',
                                                                              'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': "form-control form-control-user",
                                                                             'id': "exampleLastName",
                                                                             'placeholder': "Last Name"}))



    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['username'].widget.attrs['id'] = 'exampleFirstName'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password1'].widget.attrs['id'] = 'examplePassword1'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password2'].widget.attrs['id'] = 'examplePassword2'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat Password'


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['username'].widget.attrs['id'] = 'exampleFirstName'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['password'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password'].widget.attrs['id'] = 'examplePassword'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
