from .views import LoginPageView
from django.urls import path, include

app_name = "pages"

urlpatterns = [
    path("", LoginPageView.as_view(), name="login")
]
