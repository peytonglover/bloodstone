from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from survey.models import *
from survey.serializers import *
from django.utils import timezone

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created')
    serializer_class = SurveySerializer

    # Adapted from Django Rest Framework docs
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
    #ToDo add the rest of survey viewset

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class ResultViewSet(viewsets.ModelViewset):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer 
    