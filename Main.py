from Parameter import *

class Main:
    def main(self):
        while True:
            self.userName = input("\nEnter your user name...")
            if self.userName != "" and self.userName != " ":
                print("\n!!!Welcome, {}!!!".format(self.userName))
                while True:
                    self.option = int(input("\nDo you wish to use Auto-Decision Maker 1) Yes 2) No..."))
                    if self.option == 1:
                        self.animeList = [["Naruto", "long", "action"],
                                          ["Skip and Loafer", "short", "slice of life"],
                                          ["Haikyuu", "medium", "sports"],
                                          ["Spy x Family", "short", "action comedy"]]
                        mood(self)
                    elif self.option == 2:
                        print("\n!!!Bye, See you soon!!!")
                        quit()
                    else:
                        print("\nInvalid choice entered. Please enter a valid choice")
            else:
                print("\nInvalid user name. Please enter a valid user name")


obj1 = Main()   #Object creation
obj1.main()
