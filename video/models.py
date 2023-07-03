from django.db import models
from django.utils import timezone

class VideoContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    files = models.FileField(upload_to="files")
    thumbnail_image = models.FileField(upload_to="thumbnail", default="")

    