from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson, Question, Choice, Submission


def submit(request):
    questions = Question.objects.all()
    score = 0

    if request.method == 'POST':
        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected:
                choice = Choice.objects.get(id=selected)
                if choice.is_correct:
                    score += 1

        submission = Submission.objects.create(score=score)
        return render(
            request,
            'onlinecourse/result.html',
            {
                'score': score,
                'questions': questions
            }
        )

    return render(request, 'onlinecourse/submit.html', {'questions': questions})


def show_exam_result(request, course_id, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    course = get_object_or_404(Course, id=course_id)
    questions = Question.objects.filter(course=course)

    return render(
        request,
        'onlinecourse/result.html',
        {
            'course': course,
            'submission': submission,
            'questions': questions,
            'score': submission.score
        }
    )