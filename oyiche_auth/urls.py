# My Django imports
from django.urls import path, include

app_name = 'auth'

# My App imports
from oyiche_auth.views import *

urlpatterns = [
    path('register', RegisterView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('forgot-password', ForgotPasswordView.as_view(), name="forgot-password"),

    path('dashboard', DashboardView.as_view(), name="dashboard"),
]
