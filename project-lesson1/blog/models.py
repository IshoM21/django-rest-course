from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    user= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    
class TeamSoccer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
    number_players = models.IntegerField()
    register_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    POSITION = (
        ('P', 'Portero'),
        ('D', 'Defensa'),
        ('M', 'Mediocampista'),
        ('A', 'Atacante'),
    )
    position = models.CharField(max_length=1, choices=POSITION)
    
    
    