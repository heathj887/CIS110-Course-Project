#Greet the user and provide instructions
print(f"Hello friend.  This story is about a husband and wife and their dilemma.  Are you ready?")
print(f"Before we begin, we have questions that need answering.")
print(f"After typing your answer, be sure to press the enter key.")
input(f"\nPress the enter key to continue...")


keepPlaying = "yes"
while keepPlaying.lower() == "yes":

    #5 Questions Before the story begins
    husbandName = input(f"\nWhat is the husband's name:  ")
    while len(husbandName) == 0:
            husbandName = input(f"Please enter a man's name:  ")

    wifeName = input(f"\nWhat is the wife's name:  ")
    while len(wifeName) == 0:
            wifeName = input(f"Please enter a woman's name:  ")

    city = input(f"\nWhat is your favorite city:  ")
    while len(city) == 0:
            city = input(f"Please enter a city:  ")

    storeName = input(f"\nWhat is your favorite store:  ")
    while len(storeName) == 0:
            storeName = input(f"Please enter the name of a store:  ")

    number = input(f"\nWhat is your favorite number:  ")
    while not number.isdigit():
            number = input(f"Value not recognized.  Please enter a numeric value:  ")

    #Story Starts
    print(f"\nHere we GO!!!")
    print(f"\nOne weekend, {husbandName} and {wifeName} decided to take a drive to {city}. ")
    print(f"\n{wifeName} has always loved to go shopping. ")
    print(f"\nWhile driving down the highway, {wifeName} sees {storeName} and tells {husbandName} they should stop and go inside. ")
    print(f"\n{husbandName} knows that if he does, he will be shopping for {number} hours.  ")
    print(f"\nBut, {husbandName} also know if he doesn't, {wifeName} will get upset with him. ")

    #Decision 1
    stopAtStore = input(f"\nShould {husbandName} stop at {storeName}?  Type yes or no:  ")
    while stopAtStore.lower() != "yes" and stopAtStore.lower() != "no":
        stopAtStore = input("Please type yes or no:  ")

    if stopAtStore == "yes":
        print(f"\n{husbandName} decides to pull into the {storeName} parking lot, begrudingly. ")
        print(f"He can sense the joy on {wifeName}'s face. ")
        print(f"{husbandName} also knows he will be in {storeName} for {number} hours ")
        print(f"while {wifeName} is shopping. ")
        print(f"{husbandName} goes into {storeName} with {wifeName} to make her happy. ")
    else:
        print(f"\n{husbandName} tells {wifeName} that he has other plans for them today ")
        print(f"and continues driving past {storeName}. ")
        print(f"{wifeName} becomes very upset with him and says she told him numerous times ")
        print(f"that she NEEDED to go there! ")
        print(f"Still, {husbandName} continues to drive to {city}. ")



    print(f"As they drive past {storeName}, {husbandName} suggests they find a place to eat. ")
    print(f"His wife pouts and tells him that she doesn't really care where they go. ")
    print(f"{husbandName} knows {wifeName}'s favorite food is Mexican. ")



    #Decision 2
    goForMexican = input(f"\nShould {husbandName} take his wife for Mexican food? Type yes or no:  ")
    while goForMexican.lower() != "yes" and goForMexican.lower() != "no":
        goforMexican = input("Please type yes or no:  ")

    if goForMexican == "yes":
        print(f"\n{husbandName} decides to take his wife to a popular Mexican restaurant  ")
        print(f"for an early dinner.  She seems very pleased with his choice.  ")
        print(f"{wifeName} enjoys a couple of margaritas during dinner and forgets ")
        print(f"all about going shopping.  ")
        print(f"{husbandName} seems to have dodged a bullet...this time! ")
    else:
        print(f"\n{husbandName} pulls into the parking lot of a local Chinese restaurant. ")
        print(f"{wifeName} doesn't look too happy with his choice! ")
        print(f"During dinner, she constantly tells him they STILL need to go shopping. ")
        print(f"{husbandName} knows he will be in the doghouse for this choice! ")

     #Alternate Endings
        if stopAtStore == "yes" and goForMexican == "yes":
            print(f"\nBecause {husbandName} went shopping with {wifeName} and then took her to Mexican ")
            print(f"for dinner, she was EXTREMELY happy! ")
            print(f"{wifeName} tells him that he should go play golf with his buddies tomorrow instead ")
            print(f"of spending the day doing yard work.  {husbandName} is so excited!! ")
        elif stopAtStore == "no" and goForMexican == "no":
            print(f"\nAs a result of not going shopping with {wifeName} and taking her to a ")
            print(f"Chinese restaurant for dinner, she is very ANGRY! ") 
            print(f"{wifeName} tells him on their drive home from {city} that he will need ")
            print(f"spend the next day doing yard work that she wants done. ") 
            print(f"She also tells him that she is going on a shopping spree while he works! ")
        else:
            print(f"\nInstead of being completely upset, {wifeName} volunteers to help ")
            print(f"him with the yard work.  Because she does this, {husbandName} ")
            print(f"has time to cook up some burgers on the grill and enjoy some cold beers! ")
        print(f"\nThe End")

        keepPlaying = input(f"\nDo you want to play again? Enter yes or no:  ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
        keepPlaying = input(f"Please type yes or no:  ")

