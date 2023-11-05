from django.urls import path, include
from . import views

urlpatterns = [
    path('get', views.CharacterList.as_view()),
    path('post', views.CharacterCreate.as_view()),
]

