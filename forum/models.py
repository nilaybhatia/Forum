from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import RegexValidator
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
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
	tags = TaggableManager()
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title

class Answer(models.Model):
	answer_to = models.ForeignKey(Question, on_delete=models.CASCADE, default = None)
	text = models.TextField()
	published_date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
