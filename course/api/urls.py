from django.urls import path, include
from .views import CategoryListView

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='categories'),
]
