from django.db import models

class Survey(models.Model):
    title = models.TextField(max_length=140)
    description = models.TextField(max_length=300, null=True, blank=True)
    question = models.ManyToManyField('Question', related_name='surveys_question')
    # results = models.ForeignKey('Result', on_delete=models.CASCADE, related_name='survey_result')


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

    survey = models.ForeignKey(Survey, null=True, on_delete=models.CASCADE, related_name='questions')
    question_type = models.CharField(max_length=250, choices=TYPE_QUESTION, default=TYPE_QUESTION_TEXT)

    def __str__(self):
        return self.title

class Choice(models.Model):
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE, related_name='question_choice')
    choice_txt = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_txt


class Result(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='result_question')
    # user = models.ForeignKey('User', null=True)
    answer = models.CharField(max_length=250)

    def __str__(self):
        return self.answer





