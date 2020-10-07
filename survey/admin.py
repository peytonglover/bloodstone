from django.contrib import admin
from survey.models import *

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Result)
admin.site.register(Choice)
