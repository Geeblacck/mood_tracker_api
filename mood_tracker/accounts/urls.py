# accounts/urls.py

from django.urls import path
from .views import SignupView, RegisterView, LoginView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
