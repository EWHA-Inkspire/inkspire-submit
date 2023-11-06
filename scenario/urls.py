from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/script', ScriptView.as_view()),
    path('script/<int:pk>', ScriptListView.as_view()),
    path('script/<int:pk>/goal', GoalListView.as_view()),
    path('script/<int:pk>/goal/<int:goal_pk>', GoalDetailView.as_view()),
]
