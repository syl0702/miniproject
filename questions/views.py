from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm, CommentForm
# Create your views here.

def start(request):
    return render(request, 'start.html')


def index(request):
    questions = Question.objects.all()
    
    context = {
        'questions':questions,
    }

    return render(request, 'index.html', context)



def detail(request, id):
    question = Question.objects.get(id=id)

    comment_form = CommentForm()

    context = {
        'question': question,
        'comment_form': comment_form,
    }

    return render(request, 'detail.html', context)



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


# def choice(request, question_id):
#     user = request.user
#     question = Question.objects.get(id=question_id)

#     if question_a = 