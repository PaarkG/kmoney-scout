import ApiService

def getRoot():
    return "https://pokeapi.co/api/v2/"

def getPokemonData(name):
    url = ApiService.generateUrl(getRoot(), "pokemon/" + name)
    return ApiService.get(url)
