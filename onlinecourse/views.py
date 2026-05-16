from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
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

    submission = Submission.objects.get(
        pk=submission_id
    )

    selected_choices = submission.choices.all()

    total_score = 0

    for choice in selected_choices:

        if choice.is_correct:
            total_score += 1

    context = {
        'course': course,
        'submission': submission,
        'score': total_score,
        'choices': selected_choices,
    }

    return render(
        request,
        'onlinecourse/exam_result_bootstrap.html',
        context
    )
