from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', views.test_api),
    path('/register/', views.register_user, name='register'),
    path('/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #login
    path('/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  #renew  token
]