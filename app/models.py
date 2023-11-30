from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=20)

class Hackathons(models.Model):
    name = models.CharField(max_length=30)
    event_desc = models.TextField()
    who_can_attend = models.CharField(max_length=100) 
    duration = models.IntegerField(default=24) #duration in hrs
    opening_ceremony = models.DateTimeField()
    start_event = models.DateTimeField()
    first_round_submission = models.DateTimeField()
    second_round_submission = models.DateTimeField()
    third_round_submission = models.DateTimeField()
    winners_announcement = models.DateTimeField()
    organizers = models.ForeignKey(User,on_delete=models.CASCADE)
    rewards = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="uploads/")
    
class Status(models.Model):
    name = models.CharField(max_length=20)

class Team(models.Model):
    no_of_particpants = models.IntegerField()
    name = models.CharField(max_length=20)
    hackathon = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)

    
class Participants(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    organisation = models.CharField(max_length=30)
    age = models.IntegerField()
    