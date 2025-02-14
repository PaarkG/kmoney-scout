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
    epa = StatboticsService.getTeamYearEpa(number, 2024)
    print('processing...')
    print('considering...')
    print(epa)

# print(StatboticsService.getTeamData(1699).json())