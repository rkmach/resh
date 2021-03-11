from django.contrib.auth import forms
#estou usando o meu User, não o do django. (sobrescrevendo atributos da classe pronta!)
from .models import User
from django import forms as forms_fields

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User  

class UserCreationForm(forms.UserCreationForm):     
    class Meta(forms.UserCreationForm.Meta): 
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']

class UserChangePasswordForm(forms.PasswordChangeForm):     #descobri quais são os campos do formulário olhando o código fonte. Posso colocar css aqui também!
    old_password = forms_fields.CharField(label="Senha Antiga", max_length=50, widget=forms_fields.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms_fields.CharField(label="Nova Senha", max_length=50, widget=forms_fields.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms_fields.CharField(label="Confirme a Nova Senha", max_length=50, widget=forms_fields.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')