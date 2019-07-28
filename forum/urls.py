from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
	path('question/<int:pk>/', views.question_detail, name = 'question_detail'),
	path('question/new/', views.question_new, name = 'question_new'),
	path('question/<int:pk>/answer/', views.answer_new, name = 'answer_new'),
]
