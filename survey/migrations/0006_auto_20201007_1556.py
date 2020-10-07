# Generated by Django 3.1.2 on 2020-10-07 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20201007_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='survey.survey'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='question',
            field=models.ManyToManyField(blank=True, related_name='surveys_question', to='survey.Question'),
        ),
    ]
