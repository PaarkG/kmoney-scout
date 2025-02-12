# import PokeService

# while True:
#     response = PokeService.getPokemonData(input("Name a pokemon: "))
#     if response.status_code == 200:
#         print("Your pokemon weighs approximately " + str(round(((response.json()["weight"] * 100) / 1000) * 2.205)) + " pounds")
#     else:
#         print("Invalid pokemon name")

import StatboticsService

while True:
    number = input("number a robotics team: ")
    print('fetching...')
    print('processing...')
    print('considering...')
    response = StatboticsService.getTeamData(number)
    if response.status_code == 200:
        print(response.json()['name'])
        print('pretty chill team ngl bro')
    else:
        print("not a valid team number or the api is down :()")

print(StatboticsService.getTeamData(1699).json())