from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.urls import reverse

from .models import Course
from .models import Enrollment
from .models import Submission
from .models import Choice


def submit(request, course_id):

    course = get_object_or_404(Course, pk=course_id)

    enrollment = Enrollment.objects.get(
        user=request.user,
        course=course
    )

    selected_choices = request.POST.getlist('choice')

    submission = Submission.objects.create(
        enrollment=enrollment
    )

    choices = []

    for choice_id in selected_choices:

        choice = Choice.objects.get(id=choice_id)

        choices.append(choice)

    submission.choices.set(choices)

    return HttpResponseRedirect(
        reverse(
            'onlinecourse:show_exam_result',
            args=(course.id, submission.id)
        )
    )


def show_exam_result(request, course_id, submission_id):

    course = get_object_or_404(Course, pk=course_id)

    submission = Submission.objects.get(pk=submission_id)

    choices = submission.choices.all()

    selected_ids = []

    for choice in choices:
        selected_ids.append(choice.id)

    grade = 0
    possible_score = 0

    questions = course.question_set.all()

    for question in questions:

        possible_score += question.grade

        if question.is_get_score(selected_ids):
            grade += question.grade

    context = {
        'course': course,
        'selected_ids': selected_ids,
        'grade': grade,
        'possible': possible_score,
    }

    return render(
        request,
        'onlinecourse/exam_result_bootstrap.html',
        context
    )
