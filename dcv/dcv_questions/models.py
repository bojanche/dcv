from django.db import models

# Create your models here.


class QuestionsGroup(models.Model):
    groupName = models.CharField(max_length=200)


class Questions(models.Model):
    questionGroup = models.ForeignKey(QuestionsGroup, on_delete=models.CASCADE)
    questionText = models.CharField(max_length=500)


class Answers(models.Model):
    theQuestion = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    trueAnswer = models.BooleanField(default=False)