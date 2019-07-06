from django.contrib import admin
from .models import User, TeamMember, Question, Answer

# Register your models here.
admin.site.register(User)
admin.site.register(TeamMember)
admin.site.register(Question)
admin.site.register(Answer)
