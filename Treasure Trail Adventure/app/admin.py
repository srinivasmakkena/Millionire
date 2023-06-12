from django.contrib import admin
from .models import Question,UserRule,UserScore
from django.contrib import admin
from .models import Question, UserRule, UserScore

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'time_limit', 'award', 'options', 'answer')

@admin.register(UserRule)
class UserRuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'Max_Award', 'Max_questions')

@admin.register(UserScore)
class UserScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'userName', 'score', 'date')
# admin.site.register(Question)
# admin.site.register(UserRule)
# admin.site.register(UserScore)
