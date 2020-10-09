from django.db import models

class Survey(models.Model):
    title = models.TextField(max_length=140)
    description = models.TextField(max_length=300, null=True, blank=True)
    question = models.ManyToManyField('Question', related_name='surveys_question', blank=True)
    private_flag = models.BooleanField(default=False)
    survey_link = models.URLField()
    results = models.ManyToManyField('Result', related_name='survey_result')


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
    survey = models.ForeignKey(Survey, null=True, blank=True, on_delete=models.CASCADE, related_name='questions')
    question_type = models.CharField(max_length=250, choices=TYPE_QUESTION, default=TYPE_QUESTION_TEXT)

    def __str__(self):
        return self.question_body

class Choice(models.Model):
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE, related_name='question_choice')
    choice_body = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_txt


class Result(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='result_question')
    # user = models.ForeignKey('User', null=True)
    answer = models.ForeignKey('choice', on_delete=models.CASCADE)

    def __str__(self):
        return self.answer





