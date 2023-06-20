from django.contrib import admin

from .models import Question
from .models import Choice
from .models import Vote

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Vote)
