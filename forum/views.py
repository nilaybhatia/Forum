from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import User, TeamMember, Question, Answer
from django.shortcuts import render, get_object_or_404
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .forms import UserForm , ProfileForm
# Create your views here.

def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        #user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'forum/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form })

def create_profile(request):
    if request.method == 'POST':
        #user_form = UserForm(request.POST, instance=request.user)
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save(commit=False)
            profile_form.save(commit=False)
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect('question_list')
        
            #messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'forum/registration/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form })
def my_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('question_list')
    else:
        # Return an 'invalid login' error message.
        return render(request, 'forum/registration/login.html')
def my_logout(request):
		logout(request)
		return redirect('question_list')
#@login_required
def question_list(request):
		if request.user.is_authenticated:
			questions = Question.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
		else:
			questions = Question.objects.filter(tags__name__in=["open"]).order_by('-published_date')
		question_count = len(questions)
		return render(request, 'forum/question_list.html', {'questions': questions, 'question_count' : question_count})

def question_detail(request, pk):
		question = get_object_or_404(Question, pk = pk)
		answers = Answer.objects.filter (answer_to = question)
		answer_count = len(answers)
		return render(request, 'forum/question_detail.html', { 'question' : question, 'answers' : answers, 'answer_count' : answer_count})

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

		
		

