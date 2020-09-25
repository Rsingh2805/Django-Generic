from django.contrib import admin
from project.polls.models import Poll, Question


admin.site.register(Poll)
admin.site.register(Question)
