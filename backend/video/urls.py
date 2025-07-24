# video/urls.py

from django.urls import path
from .views import VideoPresentationListCreateView, VideoPresentationDetailView

urlpatterns = [
    path('presentations/', VideoPresentationListCreateView.as_view(), name='video-list-create'),
    path('presentations/<int:pk>/', VideoPresentationDetailView.as_view(), name='video-detail'),
]