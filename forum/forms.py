from django import forms
from .models import Question, Answer, Profile
from django.contrib.auth.models import User

class QuestionForm(forms.ModelForm):
	
	class Meta:
		model = Question
		fields = ('title', 'text', 'author', 'tags')

class AnswerForm(forms.ModelForm):

	class Meta:
		model = Answer
		fields = ('text', 'author')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date')


	
