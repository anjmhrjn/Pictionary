from django.db import models


# Create your models here.
class TeamName(models.Model):
    team_name = models.CharField(max_length=200)

    def __str__(self):
        return self.team_name


class Details(models.Model):
    team_name = models.OneToOneField(TeamName, on_delete=models.CASCADE)
    winners_in_round_one = models.BooleanField(default=True)
    winners_in_round_two = models.BooleanField(default=True)
    winners_in_round_three = models.BooleanField(default=True)
    time_in_round_one = models.IntegerField(null=True, blank=True)
    time_in_round_two = models.IntegerField(null=True, blank=True)
    avg_time_in_round_three = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.team_name)

