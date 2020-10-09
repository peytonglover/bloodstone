from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from survey.models import *
from survey.serializers import *
from django.utils import timezone

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all().order_by('-created')
    serializer_class = SurveySerializer

    #ToDo add the rest of survey viewset

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer 
    