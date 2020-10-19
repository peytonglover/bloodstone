from rest_framework import serializers
from survey.models import Survey, Question, Choice, Result

class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = [
            'url',
            'id',
            'title',
            'author',
            'description',
            'question',
            'private_flag',
            'poll_flag',
            'survey_link',
            'results',
        ]


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = [
            'url',
            'id',
            'question_body',
            'question_type',
            'option1',
            'option2',
            'option3',
            'option4',
            'option5',
        ]


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            'id',
            'question',
            'choice_body',
        ]


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = [
            'id',
            'question',
            'surveyID',
            'answer',
        ]

