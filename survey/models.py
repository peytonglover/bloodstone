from django.db import models
from django.utils import timezone
from homepage.models import CustomUser

class Survey(models.Model):
    title = models.TextField(max_length=140)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='creator')
    description = models.TextField(max_length=300, null=True, blank=True)
    question = models.ManyToManyField('Question', related_name='surveys_question', blank=True)
    private_flag = models.BooleanField(default=False)
    survey_link = models.URLField(blank=True)
    results = models.ManyToManyField('Result', related_name='survey_result', blank=True)
    created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    

class Question(models.Model):

    TYPE_QUESTION_TEXT = 'Text'
    TYPE_QUESTION_BOOL = 'Bool'
    TYPE_QUESTION_MULTIPLE_CHOICE = 'Multiple Choice'

    TYPE_QUESTION = (
        (TYPE_QUESTION_TEXT, "Text"),
        (TYPE_QUESTION_BOOL, "Bool"),
        (TYPE_QUESTION_MULTIPLE_CHOICE, "Multiple Choice")
    )

    question_body = models.CharField(max_length=250)
    survey = models.ManyToManyField(Survey, blank=True, related_name='questions')
    question_type = models.CharField(max_length=250, choices=TYPE_QUESTION, default=TYPE_QUESTION_TEXT)

    def __str__(self):
        return self.question_body

class Choice(models.Model):
    question = models.ForeignKey(Question, blank=True, on_delete=models.CASCADE, related_name='question_choice')
    choice_body = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_body


class Result(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='result_question')
    surveyID = models.ForeignKey(Survey, null=True, on_delete=models.CASCADE)
    answer = models.TextField(max_length=100)

    def __str__(self):
        return self.answer





