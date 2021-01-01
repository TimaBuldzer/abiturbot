from django.contrib import admin
from .models import Subject, SubjectTest, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_editable = ['name']


class SubjectTestAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'subject']
    search_fields = ['question']
    list_editable = ['question', 'subject']
    inlines = [AnswerInline]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'answer', 'is_right']
    search_fields = ['question', 'answer']
    list_filter = ['is_right']
    list_editable = ['question', 'answer', 'is_right']


admin.site.register(Subject, SubjectAdmin)
admin.site.register(SubjectTest, SubjectTestAdmin)
admin.site.register(Answer, AnswerAdmin)
