from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
from django.views import generic

def index(request):
    return HttpResponse("Hello world. Its Peter here")

def vote(request, number):
    message = "Number of votes is %s"
    return HttpResponse(message % number)

def query_db(request):
    list = Question.objects.all()
    response = ', '.join([q.question_text for q in list])
    return HttpResponse(response)

class ChoiceListView(generic.ListView):
    # template_name = 'core/choice_list.html'
    context_object_name = 'choices_list'

    def get_queryset(self):
        return Choice.objects.all()

     
