from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm, CommentForm
# Create your views here.

def index(request):
    questions = Question.objects.all()

    comment_form = CommentForm()

    context = {
        'questions': questions,
        'comment_form': comment_form,
    }

    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('questions:index')

    else:
        form = QuestionForm()
    
    context = {
        'form': form,
    }

    return render(request, 'form.html', context)

def comment_create(request, question_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save()
        question = Question.objects.get(id=question_id)

        comment.post = post
        comment.save()

        return redirect('questions:index')