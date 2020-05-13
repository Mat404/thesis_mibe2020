from django.urls import path
from . import views
from . import decorators


urlpatterns = [
    path("", views.homepage, name='homepage'),
    path("users/", views.UserList.as_view(), name='user_list'),
    path("user/<username>/", views.userProfileView, name='user_profile'),

]
