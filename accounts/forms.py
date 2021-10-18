from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','email','password1','password2']

        widgets = {
            'first_name':forms.TextInput(attrs={"id":"fname","class":"form-control"}),
            'last_name':forms.TextInput(attrs={"id":"lname","class":"form-control"}),
            'email':forms.TextInput(attrs={"id":"email","class":"form-control"}),
            'password1':forms.PasswordInput(attrs={"id":"password1","class":"form-control"}),
            'password2':forms.PasswordInput(attrs={"id":"password2","class":"form-control"})

        }

        labels = {
            'password2':_("Confirm Password")
        }
    def __init__(self, *args, **kwargs):
        super( RegistrationForm, self ).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class']="form-control"
        self.fields['password2'].widget.attrs['class']="form-control"
        self.fields['password1'].widget.attrs['id'] = "password1"
        self.fields['password2'].widget.attrs['id'] = "password2"
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with email already exists ")
        return email
