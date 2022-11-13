from django.shortcuts import render
from django.template import loader
from .models import QuestionsGroup, Questions, Answers
import random
# Create your views here.


def generateRandList(rand_range):
    return random.sample(range(rand_range), 5)


def index(request):
    if request.method == 'POST':
        boki = list(request.POST.items())
        print('posta', boki[1:])
    else:
        questGroup = QuestionsGroup.objects.get(pk=1)
        quests = Questions.objects.filter(questionGroup_id=questGroup.id)
        numOfQuestions = [i.id for i in quests]
        actualQuestions = random.sample(numOfQuestions, 10)
        actualQuestionsObj = Questions.objects.filter(id__in=actualQuestions)
        answers = Answers.objects.filter(theQuestion__in=actualQuestionsObj).order_by('?')


    #template = loader.get_template('dcv_questions/index.html')
    return render(request, 'dcv_questions/index.html', {'questGroup':questGroup, 'questions': actualQuestionsObj, 'answers': answers})


def page1(request):
    if request.method == 'POST':
        boki = list(request.POST.items())
        print('posta', boki[1:])
    else:
        questGroup = QuestionsGroup.objects.get(pk=2)
        quests = Questions.objects.filter(questionGroup_id=questGroup.id)
        numOfQuestions = [i.id for i in quests]
        actualQuestions = random.sample(numOfQuestions, 10)
        actualQuestionsObj = Questions.objects.filter(id__in=actualQuestions)
        answers = Answers.objects.filter(theQuestion__in=actualQuestionsObj).order_by('?')


    #template = loader.get_template('dcv_questions/index.html')
    return render(request, 'dcv_questions/index.html', {'questGroup':questGroup, 'questions': actualQuestionsObj, 'answers': answers})


def page2(request):
    if request.method == 'POST':
        boki = list(request.POST.items())
        print('posta', boki[1:])
    else:
        questGroup = QuestionsGroup.objects.get(pk=3)
        quests = Questions.objects.filter(questionGroup_id=questGroup.id)
        numOfQuestions = [i.id for i in quests]
        actualQuestions = random.sample(numOfQuestions, 10)
        actualQuestionsObj = Questions.objects.filter(id__in=actualQuestions)
        answers = Answers.objects.filter(theQuestion__in=actualQuestionsObj).order_by('?')


    #template = loader.get_template('dcv_questions/index.html')
    return render(request, 'dcv_questions/index.html', {'questGroup':questGroup, 'questions': actualQuestionsObj, 'answers': answers})


def page3(request):
    if request.method == 'POST':
        boki = list(request.POST.items())
        print('posta', boki[1:])
    else:
        questGroup = QuestionsGroup.objects.get(pk=4)
        quests = Questions.objects.filter(questionGroup_id=questGroup.id)
        numOfQuestions = [i.id for i in quests]
        actualQuestions = random.sample(numOfQuestions, 10)
        actualQuestionsObj = Questions.objects.filter(id__in=actualQuestions)
        answers = Answers.objects.filter(theQuestion__in=actualQuestionsObj).order_by('?')


    #template = loader.get_template('dcv_questions/index.html')
    return render(request, 'dcv_questions/index.html', {'questGroup':questGroup, 'questions': actualQuestionsObj, 'answers': answers})


def page4(request):
    if request.method == 'POST':
        boki = list(request.POST.items())
        print('posta', boki[1:])
    else:
        questGroup = QuestionsGroup.objects.get(pk=5)
        quests = Questions.objects.filter(questionGroup_id=questGroup.id)
        numOfQuestions = [i.id for i in quests]
        actualQuestions = random.sample(numOfQuestions, 10)
        actualQuestionsObj = Questions.objects.filter(id__in=actualQuestions)
        answers = Answers.objects.filter(theQuestion__in=actualQuestionsObj).order_by('?')


    #template = loader.get_template('dcv_questions/index.html')
    return render(request, 'dcv_questions/index.html', {'questGroup':questGroup, 'questions': actualQuestionsObj, 'answers': answers})


def page5(request):
    if request.method == 'POST':
        boki = list(request.POST.items())
        print('posta', boki[1:])
    else:
        questGroup = QuestionsGroup.objects.get(pk=6)
        quests = Questions.objects.filter(questionGroup_id=questGroup.id)
        numOfQuestions = [i.id for i in quests]
        actualQuestions = random.sample(numOfQuestions, 10)
        actualQuestionsObj = Questions.objects.filter(id__in=actualQuestions)
        answers = Answers.objects.filter(theQuestion__in=actualQuestionsObj).order_by('?')


    #template = loader.get_template('dcv_questions/index.html')
    return render(request, 'dcv_questions/index.html', {'questGroup':questGroup, 'questions': actualQuestionsObj, 'answers': answers})


def page6(request):
    if request.method == 'POST':
        boki = list(request.POST.items())
        print('posta', boki[1:])
    else:
        questGroup = QuestionsGroup.objects.get(pk=7)
        quests = Questions.objects.filter(questionGroup_id=questGroup.id)
        numOfQuestions = [i.id for i in quests]
        actualQuestions = random.sample(numOfQuestions, 10)
        actualQuestionsObj = Questions.objects.filter(id__in=actualQuestions)
        answers = Answers.objects.filter(theQuestion__in=actualQuestionsObj).order_by('?')


    #template = loader.get_template('dcv_questions/index.html')
    return render(request, 'dcv_questions/index.html', {'questGroup':questGroup, 'questions': actualQuestionsObj, 'answers': answers})


def page7(request):
    if request.method == 'POST':
        boki = list(request.POST.items())
        print('posta', boki[1:])
    else:
        questGroup = QuestionsGroup.objects.get(pk=8)
        quests = Questions.objects.filter(questionGroup_id=questGroup.id)
        numOfQuestions = [i.id for i in quests]
        actualQuestions = random.sample(numOfQuestions, 10)
        actualQuestionsObj = Questions.objects.filter(id__in=actualQuestions)
        answers = Answers.objects.filter(theQuestion__in=actualQuestionsObj).order_by('?')


    #template = loader.get_template('dcv_questions/index.html')
    return render(request, 'dcv_questions/index.html', {'questGroup':questGroup, 'questions': actualQuestionsObj, 'answers': answers})


def page8(request):
    if request.method == 'POST':
        boki = list(request.POST.items())
        print('posta', boki[1:])
    else:
        questGroup = QuestionsGroup.objects.get(pk=9)
        quests = Questions.objects.filter(questionGroup_id=questGroup.id)
        numOfQuestions = [i.id for i in quests]
        actualQuestions = random.sample(numOfQuestions, 10)
        actualQuestionsObj = Questions.objects.filter(id__in=actualQuestions)
        answers = Answers.objects.filter(theQuestion__in=actualQuestionsObj).order_by('?')


    #template = loader.get_template('dcv_questions/index.html')
    return render(request, 'dcv_questions/index.html', {'questGroup':questGroup, 'questions': actualQuestionsObj, 'answers': answers})


def page9(request):
    if request.method == 'POST':
        boki = list(request.POST.items())
        print('posta', boki[1:])
    else:
        questGroup = QuestionsGroup.objects.get(pk=10)
        quests = Questions.objects.filter(questionGroup_id=questGroup.id)
        numOfQuestions = [i.id for i in quests]
        actualQuestions = random.sample(numOfQuestions, 10)
        actualQuestionsObj = Questions.objects.filter(id__in=actualQuestions)
        answers = Answers.objects.filter(theQuestion__in=actualQuestionsObj).order_by('?')


    #template = loader.get_template('dcv_questions/index.html')
    return render(request, 'dcv_questions/index.html', {'questGroup':questGroup, 'questions': actualQuestionsObj, 'answers': answers})


def page10(request):
    if request.method == 'POST':
        boki = list(request.POST.items())
        print('posta', boki[1:])
    else:
        questGroup = QuestionsGroup.objects.get(pk=11)
        quests = Questions.objects.filter(questionGroup_id=questGroup.id)
        numOfQuestions = [i.id for i in quests]
        actualQuestions = random.sample(numOfQuestions, 4)
        actualQuestionsObj = Questions.objects.filter(id__in=actualQuestions)
        answers = Answers.objects.filter(theQuestion__in=actualQuestionsObj).order_by('?')


    #template = loader.get_template('dcv_questions/index.html')
    return render(request, 'dcv_questions/index.html', {'questGroup':questGroup, 'questions': actualQuestionsObj, 'answers': answers})


def page11(request):
    if request.method == 'POST':
        boki = list(request.POST.items())
        print('posta', boki[1:])
    else:
        questGroup = QuestionsGroup.objects.get(pk=12)
        quests = Questions.objects.filter(questionGroup_id=questGroup.id)
        numOfQuestions = [i.id for i in quests]
        actualQuestions = random.sample(numOfQuestions, 10)
        actualQuestionsObj = Questions.objects.filter(id__in=actualQuestions)
        answers = Answers.objects.filter(theQuestion__in=actualQuestionsObj).order_by('?')


    #template = loader.get_template('dcv_questions/index.html')
    return render(request, 'dcv_questions/index.html', {'questGroup':questGroup, 'questions': actualQuestionsObj, 'answers': answers})


def page12(request):
    if request.method == 'POST':
        boki = list(request.POST.items())
        print('posta', boki[1:])
    else:
        questGroup = QuestionsGroup.objects.get(pk=13)
        quests = Questions.objects.filter(questionGroup_id=questGroup.id)
        numOfQuestions = [i.id for i in quests]
        actualQuestions = random.sample(numOfQuestions, 10)
        actualQuestionsObj = Questions.objects.filter(id__in=actualQuestions)
        answers = Answers.objects.filter(theQuestion__in=actualQuestionsObj).order_by('?')


    #template = loader.get_template('dcv_questions/index.html')
    return render(request, 'dcv_questions/index.html', {'questGroup':questGroup, 'questions': actualQuestionsObj, 'answers': answers})


def page13(request):
    if request.method == 'POST':
        boki = list(request.POST.items())
        print('posta', boki[1:])
    else:
        questGroup = QuestionsGroup.objects.get(pk=14)
        quests = Questions.objects.filter(questionGroup_id=questGroup.id)
        numOfQuestions = [i.id for i in quests]
        actualQuestions = random.sample(numOfQuestions, 10)
        actualQuestionsObj = Questions.objects.filter(id__in=actualQuestions)
        answers = Answers.objects.filter(theQuestion__in=actualQuestionsObj).order_by('?')


    #template = loader.get_template('dcv_questions/index.html')
    return render(request, 'dcv_questions/index.html', {'questGroup':questGroup, 'questions': actualQuestionsObj, 'answers': answers})
    
    
def page14(request):
    if request.method == 'POST':
        boki = list(request.POST.items())
        print('posta', boki[1:])
    else:
        questGroup = QuestionsGroup.objects.get(pk=15)
        quests = Questions.objects.filter(questionGroup_id=questGroup.id)
        numOfQuestions = [i.id for i in quests]
        actualQuestions = random.sample(numOfQuestions, 10)
        actualQuestionsObj = Questions.objects.filter(id__in=actualQuestions)
        answers = Answers.objects.filter(theQuestion__in=actualQuestionsObj).order_by('?')


    #template = loader.get_template('dcv_questions/index.html')
    return render(request, 'dcv_questions/index.html', {'questGroup':questGroup, 'questions': actualQuestionsObj, 'answers': answers})