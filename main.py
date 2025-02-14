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
    print('hmmmmm')
    year = input("pick a year: ")
    print('fetching...')
    teleop = StatboticsService.getTeamYearTeleopEpa(number, year)
    print('processing...')
    auto = StatboticsService.getTeamYearAutoEpa(number, year)
    print('considering...')
    endgame = StatboticsService.getTeamYearEndgameEpa(number, year)
    print("EPA BREAKDOWN \n----------")
    print("AUTO: " + str(auto))
    print("TELEOP: " + str(teleop))
    print("ENDGAME: " + str(endgame))
    print("----------")

# print(StatboticsService.getTeamData(1699).json())