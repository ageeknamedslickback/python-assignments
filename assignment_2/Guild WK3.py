# Constant bonus added to the current power of the party to give them
# more odds of completing the adventure
BONUS_POWER = 2

def main():

    #This is the prompts and statements made for three user inputs

    print("Hello there and welcome to the Quicker Power Checker!")

    print("Please answer the following:")

    print("\nPlease enter your party size as stated on your Guild ID")

    FirstNumber=int(input("\nYour Party size is?:\t"))

    SecondNumber=int(input("\nWhat is your desired difficulty?:\t"))

    ThirdNumber=int(input("\nAnd finally, what is the AVG LVL of your party members?:\t"))



    #This is the "math" behind the scenes

    EstimatedFailure = FirstNumber*SecondNumber #Power needed

    # I have added a bonus power up, that increases the current power of the party
    # by 2 to give them more power to be strong enough for the adventure
    EstimatedSentence = FirstNumber*ThirdNumber*BONUS_POWER #Current Power



    #More statements including the outputs created

    print("\nYour estimated power needed is:",EstimatedFailure)

    print("\nYour current power is:",EstimatedSentence)



    #The three IF statements are used to identify the neccesary response.

    if(EstimatedFailure > EstimatedSentence):

        print("Oh no! You are not strong enough!")

    else:

        if(EstimatedFailure < EstimatedSentence):

            print("Congrats! You are able to go on that adventure!") #took me a minute to figure out it needed an indent... I feel dumb.

        else:

            if(EstimatedFailure == EstimatedSentence):

                print("Just barely! I would not suggest going on this adventure")

    

    #This is the final statements made to wrap up the program

    print("\nPlease keep in mind that any and all injuries sustained while on an adventure will not be used against the Guild.")

    print("Thank you for using our SySTem... ERROR ERROR ERROR... System Shutdown inevitable.")

    print("Attempted destruction of guild network is currently underway. *BOOM*")

    print("T h ANk Y Ou For Usi Ng Our Syst......")

    print("\nSystem Status: OFFLINE")

main()

