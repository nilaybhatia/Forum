from django.shortcuts import render

# Create your views here.

def question_list(request):
    return render(request, 'forum/question_list.html', {})
