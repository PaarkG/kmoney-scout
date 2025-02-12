import ApiService

def getDefaultHeaders():
    return {'accept' : 'application/json'}

def getRoot():
    return "https://api.statbotics.io/v3/"

def getApiName():
    url = ApiService.generateUrl(getRoot(), "")
    headers = getDefaultHeaders
    return ApiService.get(url, headers=headers)

def getTeamData(number=1699):
    url = ApiService.generateUrl(getRoot(), "team/" + str(number))
    headers = getDefaultHeaders()
    return ApiService.get(url, headers=headers)
    