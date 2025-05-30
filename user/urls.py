from django.urls import path
from .views import RegisterUserView, ActivateUserView, ProfileView

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('activate/', ActivateUserView.as_view()),
    path('profile/', ProfileView.as_view()),
]