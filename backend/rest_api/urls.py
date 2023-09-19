from django.urls import path, include
from .views import (
    TodoListApiView,
    sample_quote
)

urlpatterns = [
    path('', TodoListApiView.as_view()),
    path('quote/', sample_quote),
]