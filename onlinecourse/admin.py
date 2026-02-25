from django.contrib import admin
from .models import (
    Course, Lesson, Instructor, Learner,
    Question, Choice, Submission
)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'pub_date']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text',)
    inlines = [ChoiceInline]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Submission)
