from django.db import models

# Create your models here.
# Todo lo que no les guste diganlo o modifiquenlo si quieren, para que se guarde tienen que poner
# python manage.py makemigrations y despues python manage.py migrate para que se guarde en la base de datos
class Country(models.Model):
    Name = models.CharField(max_length=200)
    Code = models.CharField(max_length=200)
    Image_URL = models.CharField(max_length=200)

class League(models.Model):
    Country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    Image_URL = models.CharField(max_length=200)

class Season(models.Model):
    League = models.ForeignKey(League, null=True, on_delete=models.CASCADE)
    Year = models.IntegerField()
    Start = models.DateField()
    End = models.DateField()

class Team(models.Model):
    Name = models.CharField(max_length=200)
    Code = models.CharField(max_length=200)
    League = models.ForeignKey(League, null=True, on_delete=models.CASCADE)
    Country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)
    Image_URL = models.CharField(max_length=200)

class Stadium(models.Model):
    Country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)
    Team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    Image_URL = models.CharField(max_length=200)

class Team_Stats_Season(models.Model):
    Team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    Season = models.ForeignKey(Season, null=True, on_delete=models.CASCADE)
    Rank = models.IntegerField()
    Points = models.IntegerField()
    GoalDiff = models.IntegerField()
    Form = models.CharField(max_length=200) #esto seria wins/draws/losses
    Played = models.IntegerField()
    Wins = models.IntegerField()
    Draws = models.IntegerField()
    Losses = models.IntegerField()
    Goals_For_Home = models.IntegerField()
    Goals_For_Home_Avg = models.IntegerField()
    Goals_For_Away = models.IntegerField()
    Goals_For_Away_Avg = models.IntegerField()
    Clean_sheets = models.IntegerField() #totales

class Fixture(models.Model):
    Referee = models.CharField(max_length=200)
    Stadium = models.ForeignKey(Stadium, null=True, on_delete=models.CASCADE)
    League = models.ForeignKey(League, null=True, on_delete=models.CASCADE)
    TeamH = models.IntegerField() #ID
    TeamA = models.IntegerField() #ID (si pones 2 foreign keys de lo mismo en una misma tabla se re bugea)

class Player(models.Model):
    Firstname = models.CharField(max_length=200)
    Lastname = models.CharField(max_length=200)
    Age = models.IntegerField
    Nationality = models.CharField(max_length=200)
    Height = models.CharField(max_length=200)
    Weight = models.CharField(max_length=200)
    Injured = models.BooleanField()
    Image_URL = models.CharField(max_length=200)
    Team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)

class Bookmarker(models.Model):
    Name = models.CharField(max_length=200)

class Bet(models.Model):
    Fixture = models.ForeignKey(Fixture, null=True, on_delete=models.CASCADE)
    Bookmarker = models.ForeignKey(Bookmarker, null=True, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Value = models.CharField(max_length=200)
    Multiplier = models.IntegerField()
