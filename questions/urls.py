from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:question_id>/comments/create/', views.comment_create, name='comment_create'),
]