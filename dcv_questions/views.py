from django.shortcuts import render
from django.template import loader
from .models import QuestionsGroup, Questions, Answers
# Create your views here.


def index(request):
    questGroup = QuestionsGroup.objects.all()
    quests = Questions.objects.all()
    answers = Answers.objects.all()
    template = loader.get_template('dcv_questions/index.html')
    return render(request, 'dcv_questions/index.html', {'questGroup':questGroup, 'quests': quests, 'answers': answers})
