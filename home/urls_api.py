from django.contrib import admin
from django.urls import path
from .views_api import *

# username - admin, password - abc42802

urlpatterns = [
    path('login/', LoginView),
    path('register/',RegisterView)
]

