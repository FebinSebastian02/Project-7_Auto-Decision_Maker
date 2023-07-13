import random
def generateRandomSuggestion():
    print("\n!!!Welcome to Auto-Decision Maker!!!")
    while True:
        option = int(input("\nDo you wish to use Auto-Decision Maker 1) Yes 2) No..."))
        if option == 1:
            animeList = ["Naruto", "Skip and Loafer", "Haikyuu", "Spy x Family"]
            randomChoice = random.choice(animeList)
            print("Random suggestion:- {}".format(randomChoice))
        elif option == 2:
            print("\n!!!Bye, See you soon!!!")
            quit()
        else:
            print("\nInvalid choice entered. Please enter a valid choice")

generateRandomSuggestion()