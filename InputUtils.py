import Globals


def getSafeInputFromUser():
    userInput = input(Globals.InputPrompts.PROMPT_INPUT)
    while userInput not in ["True", "False", "exit"]:
        print("Invalid input, try again...")
        userInput = input(Globals.InputPrompts.PROMPT_INPUT)
    return userInput


def stringToBoolean(input: str) -> object:
    if input == "True":
        return True
    elif input == "False":
        return False
    else:
        return None
        