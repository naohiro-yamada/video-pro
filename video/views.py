from django.shortcuts import render, redirect
from .models import VideoContent
from .forms import VideoCreateForm

def index(request):
    videos = VideoContent.objects.all()
    context = {
        "videos": videos,
    }

    return render(request, "video/index.html", context)

def upload(request):
    if request.method == "POST":
        form = VideoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("video:index")
    else:
        form = VideoCreateForm()
    
    context = {
        "form": form
    }
    return render(request, "video/form.html", context)
    
def detail(request, video_id):
    video = VideoContent.objects.get(pk=video_id)

    context = {
        "video": video
    }

    return render(request, "video/detail.html", context)