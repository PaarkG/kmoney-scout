import TBAService

while True:
    team_number = input('number a team!!: ')
    print(TBAService.getTeamData(team_number).json()['nickname'])
