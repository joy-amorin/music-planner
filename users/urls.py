from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_api),
    path('/register/',views.register_user, name='register')
]