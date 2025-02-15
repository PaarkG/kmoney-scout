import TBAService
import StatboticsService

event_key = '2025week0'
epa_weight = 1
top_weight = .2

team_epa_dict = {}
team_avg_top_coral_dict = {}
team_net_dict = {}

def loading():
    print('chuggin ', end="", flush=True)

teams = TBAService.getEventTeams(event_key)

for team in teams:
    loading()
    team_epa_dict[team] = StatboticsService.getTeamYearEpa(team, 2025)
    loading()
    team_avg_top_coral_dict[team] = TBAService.getSeasonAverageTopCoral(team)
    loading()
    team_net_dict[team] = team_epa_dict[team] * epa_weight + team_avg_top_coral_dict[team] * top_weight

sorted_team_dict = {k: v for k, v in sorted(team_net_dict.items(), key=lambda item: item[1], reverse=True)}

print(sorted_team_dict)

print("\nTHE BEST TEAM IN THIS LIST IS " + TBAService.getTeamData(next(iter(sorted_team_dict))).json()['nickname'].upper())
