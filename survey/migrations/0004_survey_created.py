# Generated by Django 3.1.2 on 2020-10-09 01:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20201009_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]