
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('',Home.as_view(),name='home'),
     path('register/',Register.as_view(),name='register'),
     path('login/',Login.as_view(),name='login'),
     path('logout/',Logout.as_view(),name='logout'),
     path('hackathons-list/',Hackathonss.as_view(),name='hackathons'),
     path('hackathons/',HackathonsList.as_view(),name='hackathons'),
     path('single-hackathon-page/',SingleHackathonView.as_view(),name='singlehackathon'),
     path('profile/',Profile.as_view(),name='profile'),
     path('add-hackathon/',AddHackathonAPIView.as_view(),name='prosile'),

] + static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)