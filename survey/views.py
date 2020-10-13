from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from survey.models import *
from survey.serializers import *
from homepage.models import CustomUser
from django.utils import timezone


class SurveyViewSet(viewsets.ModelViewSet):

    queryset = Survey.objects.all().order_by('-created')
    serializer_class = SurveySerializer

    @action(detail=False)
    def public(self, request):
        results = Survey.objects.filter(private_flag=False)

        page = self.paginate_queryset(results)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def private(self, request):
        results = Survey.objects.filter(private_flag=True)

        page = self.paginate_queryset(results)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class UserListViewSet(viewsets.ModelViewSet):
    serializer_class = SurveySerializer

    def get_queryset(self):
        author_id = self.kwargs['author_id']
        queryset = Survey.objects.all()
        if author_id is not None:
            queryset = queryset.filter(author__id=author_id)
        return queryset
