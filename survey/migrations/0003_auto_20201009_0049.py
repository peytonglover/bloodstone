# Generated by Django 3.1.2 on 2020-10-09 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20201009_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='survey',
            field=models.ManyToManyField(blank=True, related_name='questions', to='survey.Survey'),
        ),
    ]
