'''
@author: Luke Chandra
1.1
Bugs: none
Bonuses: Loop custom list
Created on Nov 1, 2021
November 5th, 2021 Started developing the code created lists and imported .random
November 9th, 2021 Acctually created the Machine can select random sport based on the season but need to add bonuses
November 10th, 2021 Added a loop it will allow you to submit a new season 3 times and then the code will break
'''
import random
def main():
        counter = 0 
        fall = ["Football", "Soccer", "Field Hockey", "Volley Ball", "Flag Football"]
        winter = ["Basketball", "Hockey", "Wrestling"]
        spring = ["Lacrosse,", "Baseball", "Softball", "Tennis"] # Lists of all the options of sport
        while True:
            counter = counter+1
            print("Welcome to Sport-O-Matic where you tell us what season you're in and we'll pick a sport for you to play.") #an intro for when you start
            sport = input("pick a season out of fall, winter, or spring...")
            if sport == "fall":        
                print(random.choice(fall))
            elif sport == "winter":      
                print(random.choice(winter))
            elif sport == "spring":
                print(random.choice(spring)) #This is how a random part of the list is selected 
            else:
                print("Please give us one of the seasons above")
                if counter == 3:#This lets the code repeat but only 3 times and then breaks
                    break
if __name__ == '__main__':
    main()