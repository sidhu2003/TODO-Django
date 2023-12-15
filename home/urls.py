from django.urls import path
from .views import *

urlpatterns = [
    path('',TaskList.as_view()),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
]