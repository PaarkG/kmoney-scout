import ApiService

def getDefaultHeaders():
    return {'accept' : 'application/json'}

def getRoot():
    return "https://api.statbotics.io/v3/"

def getApiName():
    url = ApiService.generateUrl(getRoot(), "")
    headers = getDefaultHeaders
    return ApiService.get(url, headers=headers)

def getTeamData(endpoint='1699'):
    url = ApiService.generateUrl(getRoot(), "team/" + str(endpoint))
    headers = getDefaultHeaders()
    return ApiService.get(url, headers=headers)

def getTeamYearData(number='1699', year='2024'):
    url = ApiService.generateUrl(getRoot(), "team_year/" + str(number) + "/" + str(year))
    headers = getDefaultHeaders()
    response = ApiService.get(url, headers=headers)
    return response

def getTeamYearEpa(number='1699', year='2024'):
    response = getTeamYearData(number, year)
    team_json = response.json()
    epa_dict = team_json['epa']['total_points']
    epa = epa_dict['mean']
    return epa

def getTeamYearEpaBreakdown(number='1699', year='2024'):
    response = getTeamYearData(number, year)
    team_json = response.json()
    epa_breakdown_dict = team_json['epa']['breakdown']
    return epa_breakdown_dict

def getTeamYearAutoEpa(number='1699', year='2024'):
    epa_breakdown_dict = getTeamYearEpaBreakdown(number, year)
    auto = epa_breakdown_dict['auto_points']
    return auto

def getTeamYearTeleopEpa(number='1699', year='2024'):
    epa_breakdown_dict = getTeamYearEpaBreakdown(number, year)
    teleop = epa_breakdown_dict['teleop_points']
    return teleop

def getTeamYearEndgameEpa(number='1699', year='2024'):
    epa_breakdown_dict = getTeamYearEpaBreakdown(number, year)
    endgame = epa_breakdown_dict['endgame_points']
    return endgame

def getEventData(eventkey='2024cthar'):
    url = ApiService.generateUrl(getRoot(), "event/" + str(eventkey))
    headers = getDefaultHeaders()
    return ApiService.get(url, headers=headers)
