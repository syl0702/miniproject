from django import forms
from .models import Question, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ('user',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

