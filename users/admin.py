from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import User
from .forms import UserChangeForm, UserCreationForm

@admin.register(User)       #decotaror que registra a minha classe e diz que ela poderá definir admins.

class UserAdmin(auth_admin.UserAdmin):  #dizer pro django usar as coisas q eu defini no forms, para o meu User, não para o padrão.
    form = UserChangeForm               # # (sobrescrevendo atributos da classe padrão).
    add_form = UserCreationForm





