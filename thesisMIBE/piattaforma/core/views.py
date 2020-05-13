from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from .decorators import allowed_user


# Create your views here.
from quiz.models import Questions
from jobs.models import post_job
from functools import wraps





# @allowed_user(allowed_roles=['Admin', 'Students'])
def homepage(request):
    return render(request, 'core/homepage.html')

@allowed_user(allowed_roles=['Admin','Students'])
def userProfileView(request, username):
    user= get_object_or_404(User, username=username)
    jobs = post_job.objects.all()
    categories = Questions.CAT_CHOICES
    scores = []
    for category in categories:
        score = Questions.objects.filter(catagory=category[0], student= user).count()
        scores.append(score)

    context = {

    'user' : user, 'categories_scores' : zip( categories,scores),
    'jobs': jobs



    }
    return render(request, 'core/user_profile.html' , context)


class UserList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'core/users.html'
