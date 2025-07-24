from rest_framework import serializers
from .models import VideoPresentation

class VideoPresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPresentation
        fields = [
            'id', 'user', 'video', 'created_at', 'uploaded_at',
            'validated', 'final_validated', 'duration', 'comment'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'uploaded_at']

    def create(self, validated_data):
        user = self.context['request'].user
        if VideoPresentation.objects.filter(user=user).count() >= 3:
            raise serializers.ValidationError("You can only upload up to 3 videos.")
        return VideoPresentation.objects.create(user=user, **validated_data)
