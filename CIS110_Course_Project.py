#Greet the user and provide instructions
print(f"Hello friend.  This story is about a husband and wife and their dilemma.  Are you ready?")
print(f"Before we begin, we have questions that need answering.")
print(f"After typing your answer, be sure to press the enter key.")
input(f"\nPress the enter key to continue...")


#5 Questions Before the story begins
husbandName = input(f"\nWhat is the husband's name:  ")
wifeName = input(f"\nWhat is the wife's name:  ")
city = input(f"\nWhat is your favorite city:  ")
storeName = input(f"\nWhat is your favorite store:  ")
number = input(f"\nWhat is your favorite number:  ")
print(f"\nHere we GO!!!")
print(f"\nOne weekend, {husbandName} and {wifeName} decided to take a drive to {city}. ")
print(f"\n{wifeName} has always loved to go shopping. ")

 #Story Starts
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
    print(f"\n{husbanName} tells {wifeName} that he has other plans for them today ")
    print(f"and continues driving past {storeName}. ")
    print(f"{wifeName} becomes very upset with him and says she told him numerous times ")
    print(f"that she NEEDED to go there! ")
    print(f"Still, {husbandName} continues to drive to {city}. ")



