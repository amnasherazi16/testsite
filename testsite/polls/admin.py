from django.contrib import admin
from polls.models import Choice, Question

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.autodiscover()

