from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
	path('login/', views.my_login, name = 'my_login'),
	path('logout/', views.my_logout, name = 'my_logout'),
	path('signup/', views.create_profile, name = 'create_profile'),
	path('accounts/profile/', views.question_list, name = 'question_list'),
	path('question/<int:pk>/', views.question_detail, name = 'question_detail'),
	path('question/new/', views.question_new, name = 'question_new'),
	path('question/<int:pk>/answer/', views.answer_new, name = 'answer_new'),
	path('question/<int:pk>/edit/', views.question_edit, name = 'question_edit'),
	path('answer/<int:pk>/edit/', views.answer_edit, name = 'answer_edit'),
	path('question/<int:pk>/upvote/', views.upvote, name = 'upvote'),
	path('question/<int:pk>/downvote', views.downvote, name = 'downvote'),
]
