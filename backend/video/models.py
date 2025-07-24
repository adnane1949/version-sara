from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

def video_upload_path(instance, filename):
    import uuid
    ext = filename.split('.')[-1]
    return f"videos/user_{instance.user_id}/{uuid.uuid4()}.{ext}"

class VideoPresentation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="video_presentations"
    )
    video = models.FileField(upload_to=video_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(blank=True, null=True)
    validated = models.BooleanField(default=False)         # Candidate clicked validate
    final_validated = models.BooleanField(default=False)   # Candidate made it "official"
    duration = models.DurationField(blank=True, null=True) # Optional: can be filled later
    comment = models.TextField(blank=True, null=True)      # Optional: admin/review note

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Video {self.id} by {getattr(self.user, 'username', self.user_id)}"
    
