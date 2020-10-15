from django.urls import path
from .login_view import login, signup

# Maps the login function to position /login from base url i.e. 127.0.0.1:8000/login
urlpatterns = [
    path('login', login, name='login'),
    path('signup', signup, name='signup')
]