from django.contrib import admin
from . models import Question, Choice


class ChoiceInline(models.stackInline):
	extra = 1
	choices = Choice

class QuestionAdmin(admin.ModelAdmin):
	list_display = ("question_text","pub_date")
	inlines = ChoiceInline
admin.site.register(Question, QuestionAdmin)


