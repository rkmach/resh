from django.contrib.auth import forms

from .models import User

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User        #estou usando o meu User, não o do django. (sobrescrevendo atributos da classe pronta!)



class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta): 
        model = User