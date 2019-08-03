from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.
alphanumeric = RegexValidator(r'^[0-9a-zA-Z_-]*$', 'Only alphanumeric characters are allowed.')
class User(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	username = models.CharField(max_length = 10, unique=True, validators=[alphanumeric])
	YEAR_CHOICES = [('FE', '1st year'), ('SE', '2nd year'), ('TE', '3rd year'), ('BE', '4th year')]
	year = models.CharField(max_length = 2, choices = YEAR_CHOICES) 
	def __str__(self):
		return self.username

class TeamMember(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	username = models.CharField(max_length = 10, unique=True, validators=[alphanumeric])
	department = models.CharField(max_length = 20)
	def __str__(self):
		return self.username

class Question(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	published_date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title

class Answer(models.Model):
	answer_to = models.ForeignKey(Question, on_delete=models.CASCADE, default = None)
	upvotes = models.IntegerField()
	text = models.TextField()
	published_date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
