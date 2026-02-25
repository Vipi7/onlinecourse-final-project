def show_exam_result(request, course_id, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    selected_ids = submission.choices.values_list('id', flat=True)

    total_score = 0
    possible_score = 0

    for question in Question.objects.filter(lesson__course_id=course_id):
        possible_score += 1
        if question.is_get_score(selected_ids):
            total_score += 1

    grade = total_score / possible_score * 100

    context = {
        'selected_ids': selected_ids,
        'grade': grade,
        'possible': possible_score,
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
