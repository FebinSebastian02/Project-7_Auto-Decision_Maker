def mood(self):
    while True:
        mood = int(input("\nEnter your mood 1) Bored 2) Energetic 3) Nostalgic..."))
        if mood == 1:
            for i in self.animeList:
                if (i[1] == "long" or i[1] == "short") and (i[2] == "action" or i[2] == "action comedy"):
                    print("Recommended suggestion is :- {}".format(i[0]))
            break
        elif mood == 2:
            for i in self.animeList:
                if i[1] == "medium" and i[2] == "sports":
                    print("Recommended suggestion is:- {}".format(i[0]))
            break
        elif mood == 3:
            for i in self.animeList:
                if i[1] == "short" and i[2] == "slice of life":
                    print("Recommended suggestions is:- {}".format(i[0]))
            break
        else:
            print("\nInvalid option entered. Enter a valid option...")