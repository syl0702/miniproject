from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('start/', views.start, name='start'),
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:question_id>/comments/create/', views.comment_create, name='comment_create'),
]