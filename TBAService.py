import ApiService

API_KEY = 'zoCvkoEWbJznmV4Fklyt6uBtELignKKwqtliLdWwVpVIb6CAWWfgazNMhlBYsRJO'

def getDefaultHeaders():
    return {'accept' : 'application/json', 'X-TBA-Auth-Key' : API_KEY}

def getRoot():
    return "https://www.thebluealliance.com/api/v3/"

def getStatus():
    url = ApiService.generateUrl(getRoot(), 'status')
    headers = getDefaultHeaders()
    response = ApiService.get(url, headers=headers)
    return response

def getTeamData(number='1699'):
    url = ApiService.generateUrl(getRoot(), 'team/frc' + str(number))
    headers = getDefaultHeaders()
    response = ApiService.get(url, headers=headers)
    return response

def getTeamSeasonEventKeys(number='1699', year=2025):
    url = ApiService.generateUrl(getRoot(), 'team/frc' + str(number) + "/events/" + str(year))
    headers = getDefaultHeaders()
    response = ApiService.get(url, headers=headers)
    event_json = response.json()
    keys = []
    for event in event_json:
        keys.append(event['key'])
    return keys

def getTeamSeasonMatchData(number='1699', event_keys=['2025mawor', '2025rikin']):
    match_data = []
    for event_key in event_keys:
        url = ApiService.generateUrl(getRoot(), 'team/frc' + str(number) + "/event/" + event_key + '/matches')
        headers = getDefaultHeaders()
        response = ApiService.get(url, headers=headers)
        match_data.append(response.json())
    return match_data

def getReefDict(match, alliance='blue'):
    reef_dict = {}
    score_breakdown = match['score_breakdown']
    alliance_breakdown = score_breakdown[alliance]
    reef_dict['auto'] = alliance_breakdown['autoReef']
    reef_dict['teleop'] = alliance_breakdown['teleopReef']
    return reef_dict
        
def getTopCoral(reef_dict):
    number_scored = 0
    auto = reef_dict['auto']
    top_auto = auto['topRow']
    for node in top_auto:
        if top_auto[node] == True:
            print(node)
            number_scored += 1
    teleop = reef_dict['teleop']
    top_teleop = teleop['topRow']
    for node in top_teleop:
        if top_teleop[node] == True:
            number_scored += 1
    return number_scored

def getMidCoral(reef_dict):
    number_scored = 0
    auto = reef_dict['auto']
    mid_auto = auto['midRow']
    for node in mid_auto:
        if mid_auto[node] == True:
            number_scored += 1
    teleop = reef_dict['teleop']
    mid_teleop = teleop['midRow']
    for node in mid_teleop:
        if mid_teleop[node] == True:
            number_scored += 1
    return number_scored

def getBotCoral(reef_dict):
    number_scored = 0
    auto = reef_dict['auto']
    bot_auto = auto['botRow']
    for node in bot_auto:
        if bot_auto[node] == True:
            number_scored += 1
    teleop = reef_dict['teleop']
    bot_teleop = teleop['botRow']
    for node in bot_teleop:
        if bot_teleop[node] == True:
            number_scored += 1
    return number_scored

def getAverageTopCoral(number='1699', event_key='2025week0'):
    number_matches = 0
    number_coral = 0
    match_data = getTeamSeasonMatchData(number, [event_key])[0]
    for match in match_data:
        reef_dict = None
        if 'frc' + str(number) in match['alliances']['blue']:
            reef_dict = getReefDict(match, 'blue')
        else:
            reef_dict = getReefDict(match, 'red')
        number_coral += getTopCoral(reef_dict)
        number_matches += 1
    return float(number_coral) / float(number_matches)

print(getAverageTopCoral(97, '2025week0'))

