from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import User, TeamMember, Question, Answer
from django.shortcuts import render, get_object_or_404
from .forms import QuestionForm, AnswerForm
import requests, re

# Create your views here.
def call_stackoverflow_API(language_tag):
	response = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=creation' + language_tag + '&site=stackoverflow')
	copy = []
	#print (response.json())
	for data in response.json()['items']:
		data_dic = {}
		data_dic['title'] = data['title']
		data_dic['link'] = data['link']
		copy.append(data_dic)
	return copy

def question_list(request):
		questions = Question.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
		question_count = len(questions)
		stack_overflow_data = call_stackoverflow_API('')
		return render(request, 'forum/question_list.html', {'questions': questions, 'question_count' : question_count, 'stack_overflow_data' : stack_overflow_data})

def question_detail(request, pk):
		question = get_object_or_404(Question, pk = pk)
		answers = Answer.objects.filter (answer_to = question).order_by('-upvotes')
		answer_count = len(answers)
		languages_or_frameworks = ["java", "python", "c", "cpp", "django", "android", "ruby"]
		words = (question.title).split(' ')
		words = re.split(r'[\s,\?\.]', question.title)
		print (words)
		language=''
		for word in words:
			if word.lower() in languages_or_frameworks:
				language = word
				break
		print("Hello" + language)
		stack_overflow_data = call_stackoverflow_API('&tagged=' + language)
		return render(request, 'forum/question_detail.html', { 'question' : question, 'answers' : answers, 'answer_count' : answer_count, 'stack_overflow_data' : stack_overflow_data, 'lang':language})

def question_new(request):
	if request.method == "POST":
		form = QuestionForm(request.POST)
		if form.is_valid():
			question = form.save(commit = False)
			question.published_date = timezone.now()
			question.save()
			return redirect('question_detail', pk = question.pk)
	else:
		form = QuestionForm()
	return render(request, 'forum/question_edit.html', {'form' : form})

def answer_new(request, pk):
	if request.method == "POST":
		form = AnswerForm(request.POST)
		if form.is_valid():
			answer = form.save(commit = False)
			answer.published_date = timezone.now()
			question = get_object_or_404(Question, pk = pk)
			answer.answer_to = question
			answer.upvotes=0
			answer.save()
			return redirect('question_detail', pk = question.pk)
	else:
		form = AnswerForm()
		question = get_object_or_404(Question, pk = pk)
	return render(request, 'forum/answer_edit.html', {'form':form, 'question' : question})

def question_edit(request, pk):
    question = get_object_or_404(Question, pk = pk)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.published_date = timezone.now()
            question.save()
            return redirect('question_detail', pk = question.pk)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'forum/question_edit.html', {'form': form})

def answer_edit(request, pk): #pk is primary key of answer to be edited 
	answer = get_object_or_404(Answer, pk = pk)
	question = answer.answer_to
	if request.method == "POST":
		form = AnswerForm(request.POST, instance=answer)
		if form.is_valid():
			answer = form.save(commit = False)
			answer.published_date = timezone.now()
			answer.answer_to = question
			answer.save()
			return redirect('question_detail', pk = question.pk)
	else:
		form = AnswerForm(instance=answer)
	return render(request, 'forum/answer_edit.html', {'form':form, 'question' : question})

def upvote(request, pk):
	answer = get_object_or_404(Answer, pk=pk)
	question = answer.answer_to
	answer.upvotes += 1
	answer.save()
	return redirect('question_detail', pk = question.pk)

def downvote(request, pk):
	answer = get_object_or_404(Answer, pk=pk)
	question = answer.answer_to
	answer.upvotes -= 1
	answer.save()
	return redirect('question_detail', pk = question.pk)





		
		

