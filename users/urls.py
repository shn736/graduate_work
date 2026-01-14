from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (UserCreateApiView, UserDestroyApiView,
                         UserListApiView, UserRetrieveApiView,
                         UserUpdateApiView)

app_name = UsersConfig.name

urlpatterns = [
    path(
        "register/",
        UserCreateApiView.as_view(permission_classes=(AllowAny,)),
        name="register",
    ),
    path(
        "login/",
        TokenObtainPairView.as_view(),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("user/", UserListApiView.as_view(), name="user_list"),
    path("user/<int:pk>/", UserRetrieveApiView.as_view(), name="user_retrieve"),
    path(
        "user/<int:pk>/delete/",
        UserDestroyApiView.as_view(),
        name="user_delete",
    ),
    path(
        "user/<int:pk>/update/",
        UserUpdateApiView.as_view(),
        name="user_update",
    ),
]
