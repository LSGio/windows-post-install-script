

def getSafeInputFromUser():
    userInput = "null"
    while userInput not in ["True", "False", "exit"]:
        print("Invalid input, try again...")
        userInput = input("Your input : ")
    return userInput