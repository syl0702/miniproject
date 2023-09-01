from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    question_a = models.TextField()
    question_b = models.TextField()

class Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)