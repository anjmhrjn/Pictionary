from django.shortcuts import render
from .models import TeamName, Details


# Create your views here.
def scores(request):
    team_one = request.GET.get("team1")
    team_two = request.GET.get("team2")
    two_teams = [team_one, team_two]

    total_teams = Details.objects.filter(winners_in_round_one=True).filter(winners_in_round_two=True)

    if request.method == 'POST':

        winner_team = request.POST.get("winner")
        winner_id = TeamName.objects.get(team_name=winner_team)

        temp = []
        temp.extend(two_teams)
        temp.remove(winner_team)
        lost_team = temp[0]

        loser_id = TeamName.objects.get(team_name=lost_team)

        time_taken = int(request.POST.get("time"))
        game_round = request.POST.get("round")

        time_in_round1 = None
        time_in_round2 = None
        time_in_round3 = None

        if game_round == 'RoundOne':
            Details.objects.filter(team_name=loser_id).update(winners_in_round_one=False)
            time_in_round1 = time_taken
        elif game_round == 'RoundTwo':
            Details.objects.filter(team_name=loser_id).update(winners_in_round_two=False)
            time_in_round2 = time_taken
        elif game_round == 'RoundThree':

            time_in_round3 = time_taken

        filtered_team = Details.objects.filter(team_name=winner_id)

        if time_in_round1 is not None:
            filtered_team.update(time_in_round_one=time_in_round1)

        elif time_in_round2 is not None:
            filtered_team.update(time_in_round_two=time_in_round2)

        elif time_in_round3 is not None:
            time_from_db = Details.objects.get(
                team_name=TeamName.objects.get(team_name=winner_id)).avg_time_in_round_three
            if time_from_db is None:
                filtered_team.update(avg_time_in_round_three=time_in_round3)
            else:
                avg_time = (time_from_db + time_in_round3)/2
                filtered_team.update(avg_time_in_round_three=avg_time)

    context = {
        "teams": total_teams,
        "two_teams": two_teams,
        "details": Details.objects.all(),
    }
    return render(request, 'scoreboard/orientation.html', context)
