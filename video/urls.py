from django.urls import path
from . import views


app_name = "video"

urlpatterns = [
    path("", views.index, name="index"),
    path("upload/", views.upload, name="upload"),
    path("<int:video_id>/detail/", views.detail, name="detail")
]

