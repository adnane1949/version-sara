from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import VideoPresentation
from .serializers import VideoPresentationSerializer

# Create your views here.

class VideoPresentationListCreateView(generics.ListCreateAPIView):
    serializer_class = VideoPresentationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return VideoPresentation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VideoPresentationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VideoPresentationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return VideoPresentation.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        final_validated = self.request.data.get('final_validated', None)
        if final_validated is True or final_validated == 'true':
            VideoPresentation.objects.filter(
                user=self.request.user
            ).update(final_validated=False)
        serializer.save()
