from django.db import models

# Create your models here.
class Team(models.Model):
    name=models.CharField(max_length=100)
    odds=models.FloatField()
    home=models.BooleanField()
class Game(models.Model):
    hometeam=models.ForeignKey(Team,related_name='hometeam',on_delete=models.CASCADE)
    awayteam=models.ForeignKey(Team,related_name='awayteam',on_delete=models.CASCADE)
    matchdate=models.DateField()

