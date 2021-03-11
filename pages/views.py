from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from users.forms import UserCreationForm, UserChangePasswordForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy



class InitialPageView(TemplateView):
    template_name = "initial.html"

class HomePageView(TemplateView):
    template_name = "home.html"

class LoginPageView(LoginView):
    template_name = "login.html"

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


class PasswordChangePageView(PasswordChangeView):
    template_name = "change_password.html"
    form_class = UserChangePasswordForm
    success_url = reverse_lazy('pages:success_changed_pass')

def success_changed_password(response):
    return render(response, 'success_changed_password.html', {})


