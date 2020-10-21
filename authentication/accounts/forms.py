from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import Account


class StudentRegistration(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = (
            'email',
            'fullname',
            'department',
            'student_id',
            'password1',
            'password2',
        )


class StudentLoginForm(forms.Form):
    class Mete:
        model = Account
        fields = (
            'email',
            'password'
        )

        def clean(self):
            if self.is_valid():
                email = self.cleaned_data['email']
                password = self.cleaned_data['password']
                if not authenticate(email=email, password=password):
                    raise forms.ValidationError("Invalid login")



class StudentEditProfileForm(UserChangeForm):
    class Meta:
        model = Account
        fields = (
            'email',
            'fullname',
            'student_id',
            'department',
            'image',
        )


