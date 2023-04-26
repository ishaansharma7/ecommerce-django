from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import AllUsers

class SignUpForm(UserCreationForm):
    password2 = forms.PasswordInput()

    class Meta:
        model = AllUsers 
        fields = ('email', 'password1', 'password2', 'first_name', 'phone_number', 'address', )
    
    def save(self, **kwargs):
        
        password = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError({'password': 'passwords does not match'})
        
        new_user = AllUsers.objects.create_user(email=self.cleaned_data['email'],
                            first_name=self.cleaned_data['first_name'], 
                            phone_number=self.cleaned_data['phone_number'],
                            address=self.cleaned_data['address'],
                            password=password)

        return new_user