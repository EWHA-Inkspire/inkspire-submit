from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/script', ScriptView.as_view())
]
