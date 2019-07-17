from django.db import models

# Create your models here.
class Team(models.Model):
    name=models.CharField(max_length='100')
    odds=models.FloatField()
    home=models.BooleanField()
class Game(models.Model):
    hometeam=models.ForeignKey(Team,on_delete=models.CASCADE)
    awayteam=models.ForeignKey(Team,on_delete=models.CASCADE)
    matchdate=models.DateField()

