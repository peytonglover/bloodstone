from rest_framework import serializers
from survey.models import Survey, Question, Choice, Result

class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = [
            'id',
            'title',
            'author',
            'description',
            'question',
            'private_flag',
            'survey_link',
            'results',
        ]


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'question_body',
            'survey',
            'question_type',
        ]

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = [
            'id',
            'question',
            'choice_body',
        ]

class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = [
            'id',
            'question',
            'surveyID',
            'answer',
        ]

