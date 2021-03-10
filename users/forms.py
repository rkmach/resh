from django.contrib.auth import forms
#estou usando o meu User, não o do django. (sobrescrevendo atributos da classe pronta!)
from .models import User
from django.forms import ModelForm


class MeuForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password'] 

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User  

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta): 
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']

class UserAuthenticationForm(forms.AuthenticationForm):
    pass
