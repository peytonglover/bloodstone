from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import UserSerializer
from homepage.models import CustomUser

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

