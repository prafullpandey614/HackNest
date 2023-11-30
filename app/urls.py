
from django.urls import path
from .views import *
urlpatterns = [
     path('home/',Home.as_view(),name='home'),
     path('register/',Register.as_view(),name='register'),
     path('login/',Login.as_view(),name='login'),
     path('logout/',Logout.as_view(),name='logout'),
     path('hackathons/',Hackathons.as_view(),name='hackathons'),
     path('single-hackathon-page/',SingleHackathonView.as_view(),name='singlehackathon'),
     path('profile/',Profile.as_view(),name='profile'),
]
