from .views import InitialPageView, LoginPageView, LogoutPageView, HomePageView, register, PasswordChangePageView, success_changed_password
from django.urls import path, include

app_name = "pages"

urlpatterns = [
    path("", InitialPageView.as_view(), name="initial"),
    path("login/", LoginPageView.as_view(), name="login"),
    path("home/", HomePageView.as_view(), name="home"),
    path("logout/", LogoutPageView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("changePassword/", PasswordChangePageView.as_view(), name="change_password"),
    path("successfully_changed_password/", success_changed_password, name="success_changed_pass"),
]
