from django.db import models

# Create your models here.
class Season(models.Model):
    season=models.IntegerField()
    city=models.CharField(max_length=128,null=True,blank=True)
    team1 = models.CharField(max_length=128,null=True,blank=True)
    team2= models.CharField(max_length=128,null=True,blank=True)
    toss_winner = models.CharField(max_length=128,null=True,blank=True)
    toss_decision = models.CharField(max_length=128,null=True,blank=True)
    result = models.CharField(max_length=128,null=True,blank=True)
    dl_applied=models.BooleanField()
    winner = models.CharField(max_length=128,null=True,blank=True)
    winner_by_runs = models.IntegerField()
    winner_by_wickets = models.IntegerField()
    player_of_the_match = models.CharField(max_length=128,null=True,blank=True)
    venue = models.CharField(max_length=128,null=True,blank=True)
    umpire1 = models.CharField(max_length=128,null=True,blank=True)
    umpire2= models.CharField(max_length=128,null=True,blank=True)
    umpire3= models.CharField(max_length=128,null=True,blank=True)

    def __str__(self):
        return self.season


class Match(models.Model):
    match=models.ForeignKey(Season, on_delete=models.CASCADE)
    inning=models.IntegerField()
    batting_team = models.CharField(max_length=128,null=True,blank=True)
    bowling_team = models.CharField(max_length=128,null=True,blank=True)
    over = models.IntegerField()
    ball = models.IntegerField()
    batsman = models.CharField(max_length=128,null=True,blank=True)
    non_striker = models.CharField(max_length=128,null=True,blank=True)
    bowler = models.CharField(max_length=128,null=True,blank=True)
    is_super_over = models.BooleanField()
    wide_runs = models.IntegerField()
    bye_runs = models.IntegerField()
    legbye_runs = models.IntegerField()
    noball_runs = models.IntegerField()
    penalty_runs = models.IntegerField()
    batsman_runs = models.IntegerField()
    extra_runs = models.IntegerField()
    total_runs = models.IntegerField()
    player_dismissed = models.CharField(max_length=128,null=True,blank=True)
    dismissal_kind = models.CharField(max_length=128,null=True,blank=True)
    fielder = models.CharField(max_length=128,null=True,blank=True)

    def __str__(self):
        return self.match_id

