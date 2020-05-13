from django.urls import path, re_path, include
from . import views

# urlpatterns = [
#                 path("quiz/", views.quiz, name='quiz'),
#                 path("questions/<choice>/", views.questions, name='questions'),
#                 path("result/", views.result, name='result'),
#
# ]

urlpatterns = [
    re_path(r'^quiz', views.quiz, name = 'quiz'),
    re_path(r'^result', views.result, name = 'result'),
    re_path(r'^(?P<choice>[\w]+)', views.questions, name = 'questions'),
]
