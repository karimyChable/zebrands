from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from zebrands.users.views import UserView, UserListView

users_url = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Endpoints for users
    path("users/<int:pk>", UserView.as_view()),
    path("users/", UserListView.as_view()),
]
