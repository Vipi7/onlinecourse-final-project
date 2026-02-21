from django.shortcuts import render
from .models import Question, Choice

def submit(request):
    questions = Question.objects.all()

    if request.method == 'POST':
        score = 0
        total = questions.count()

        for q in questions:
            selected = request.POST.get(str(q.id))
            if selected:
                choice = Choice.objects.get(id=int(selected))
                if choice.is_correct:
                    score += 1

        return render(request, 'onlinecourse/result.html', {
            'score': score,
            'total': total
        })

    return render(request, 'onlinecourse/submit.html', {'questions': questions})