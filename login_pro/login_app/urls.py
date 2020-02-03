from django.urls import path
from login_app import views

app_name = 'login_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
]