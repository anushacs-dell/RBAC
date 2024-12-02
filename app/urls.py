from django.urls import path
from.views import*
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('admin',admin_view),
    path('user',user_view),
    path('moderator',moderator_view),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('logout', LogoutView.as_view()),
]
