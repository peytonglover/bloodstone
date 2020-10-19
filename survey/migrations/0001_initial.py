# Generated by Django 3.1.2 on 2020-10-19 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_body', models.CharField(max_length=250)),
                ('question_type', models.CharField(choices=[('Text', 'Text'), ('Bool', 'Bool'), ('Multiple Choice', 'Multiple Choice')], default='Text', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=100)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_question', to='survey.question')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=140)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('private_flag', models.BooleanField(default=False)),
                ('poll_flag', models.BooleanField(default=True)),
                ('survey_link', models.URLField(blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('question', models.ManyToManyField(blank=True, related_name='surveys_question', to='survey.Question')),
                ('results', models.ManyToManyField(blank=True, related_name='survey_result', to='survey.Result')),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='surveyID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.survey'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_body', models.CharField(max_length=200)),
                ('question', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_choice', to='survey.question')),
            ],
        ),
    ]
