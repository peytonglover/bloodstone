"""capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from survey import views as survey_views
from homepage import views as homepage_views

router = routers.DefaultRouter()
router.register(r'survey', survey_views.SurveyViewSet)
router.register(r'question', survey_views.QuestionViewSet)
router.register(r'choice', survey_views.ChoiceViewSet)
router.register(r'result', survey_views.ResultViewSet)
router.register(r'user', homepage_views.CustomUserViewSet)
router.register(r'survey-list/(?P<author_id>\d+)', survey_views.UserListViewSet, basename='list')



urlpatterns = [
    path('api/auth/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
