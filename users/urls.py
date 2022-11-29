from django.urls import path
from users.views import register

urlpatterns = [
    path('', register, name='register'),
    path('register/', register, name='register'),
]
