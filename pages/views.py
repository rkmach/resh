from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import MeuForm, UserCreationForm
from django.contrib.auth import authenticate, login



class InitialPageView(TemplateView):
    template_name = "initial.html"

class HomePageView(TemplateView):
    template_name = "home.html"

class LoginPageView(LoginView):
    template_name = "login.html"
    #form_class = MeuForm

class LogoutPageView(LogoutView):
    pass

def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
            login(response, new_user)
            return redirect("../home")
    else:
        form = UserCreationForm()
    return render(response, "register.html", {"form": form})

