from django.urls import path
from . import views


urlpatterns = [
    path("", views.viz_job, name='jobs'),
    path("creation/", views.creapost, name='jobs'),
    path("submit/", views.creapost, name='submit'),



]
