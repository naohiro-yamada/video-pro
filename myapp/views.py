from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return render(request, "myapp/index.html", context)

class IndexView(generic.ListView):
    template_name = "myapp/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

# ver.1
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exit")
#     return render(request, "myapp/detail.html", {"question": question})

# ver.2
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "myapp/detail.html", {"question": question})

class DetailView(generic.DetailView):
    model = Question
    template_name = "myapp/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "myapp/results.html", {"question": question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = "myapp/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "myapp/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("myapp:results", args=(question.id,)))