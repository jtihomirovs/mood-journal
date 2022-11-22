from django.urls import path
from django.conf import settings
from authentication.views import UserCreate, LoginView, LogoutView, ProfileView, SessionCheckView

urlpatterns = [
    path('account/register/', UserCreate.as_view()),
    path('account/login/', LoginView.as_view()),
    path('account/logout/', LogoutView.as_view()),
    path('account/profile/', ProfileView.as_view()),
    path('account/session/', SessionCheckView.as_view()),
]
