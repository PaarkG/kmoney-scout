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

def getTeamYearEpa(number='1699', year='2024'):
    url = ApiService.generateUrl(getRoot(), "team_year/" + str(number) + "/" + str(year))
    headers = getDefaultHeaders()
    response = ApiService.get(url, headers=headers)
    if response.status_code == 200:
        team_json = response.json()
        epa_dict = team_json['epa']['total_points']
        epa = epa_dict['mean']
        return float(epa)

def getEventData(eventkey='2024cthar'):
    url = ApiService.generateUrl(getRoot(), "event/" + str(eventkey))
    headers = getDefaultHeaders()
    return ApiService.get(url, headers=headers)
