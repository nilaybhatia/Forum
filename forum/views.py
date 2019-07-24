from django.shortcuts import render
from django.utils import timezone
from .models import User, TeamMember, Question, Answer
from django.shortcuts import render, get_object_or_404

# Create your views here.

def question_list(request):
		questions = Question.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
		return render(request, 'forum/question_list.html', {'questions': questions})

def question_detail(request, pk):
		question = get_object_or_404(Question, pk = pk)
		answers = Answer.objects.filter (answer_to = question)
		answer_count = len(answers)
		return render(request, 'forum/question_detail.html', { 'question' : question, 'answers' : answers, 'answer_count' : answer_count})

