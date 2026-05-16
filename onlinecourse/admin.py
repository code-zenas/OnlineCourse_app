from django.contrib import admin

from .models import (
    Course,
    Lesson,
    Enrollment,
    Question,
    Choice,
    Submission,
)

# Choice Inline
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


# Question Inline
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order']


# Register Models
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
