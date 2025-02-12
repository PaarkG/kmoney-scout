from PokeService import PokeService

while True:
    response = PokeService.getPokemonData(input("Name a pokemon: "))
    if response.status_code == 200:
        print(response.json()["name"])
    else:
        print("INVALID POKEMON NAME, TRY AGAIN IDIOT")
