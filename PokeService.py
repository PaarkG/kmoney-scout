from ApiService import ApiService

class PokeService:
    @staticmethod
    def getRoot():
        return "https://pokeapi.co/api/v2/"

    @staticmethod
    def getPokemonData(name):
        url = ApiService.generateUrl(PokeService.getRoot(), "pokemon/" + name)
        return ApiService.get(url)
