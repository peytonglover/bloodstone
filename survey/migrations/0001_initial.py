# Generated by Django 3.1.2 on 2020-10-07 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('Text', 'Text'), ('Bool', 'Bool'), ('Multiple Choice', 'Multiple Choice')], default='Text', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=140)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('question', models.ManyToManyField(related_name='surveys_question', to='survey.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=250)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_question', to='survey.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='survey.survey'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_txt', models.CharField(max_length=200)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_choice', to='survey.question')),
            ],
        ),
    ]
