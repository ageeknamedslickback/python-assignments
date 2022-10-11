# Python Code
# This program will calculate and display the total monthly pay for each professional barber.
# The user will be prompted for the number of haircuts in a single shift, the number of days hair cuts is serviced per month, and the amount of tips recieved for the month.
# The program will accumulate and display Shop Totals ( sum of all professional barbers)

# Developer: Eric Alexander II CMIS102/6986 Wk2 Discussion Date: June 27, 2022
# Modified: EDA - modified for If Statements    July 03, 2022
# Modified: EDA - modified for Functions        July 09, 2022
# Modified: EDA - modified for Loops            July 15, 2022

# Define Functions
# Display Welcome message


# Change made by Jonathan Weaver
# The total number of baber working days in a month
WORKING_DAYS_IN_A_MONTH = 20


def WelcomeMessage():
    # This function displays the Welcome message
    print("\nWelcome to Cutthroat Island barber service program")
    print(
        "\nThis program will calculate the total monthly shop pay, including tips and commission"
    )


# Prompt the user for number of haircuts in a single shift and Get the user response
def GetNumHair():
    numHAIR = input(
        "\n How many haircuts did you service today(Few, Several, Many)? \t   "
    )
    return numHAIR


# Prompt the user for number of days hair cuts is serviced per month and Get the user response
def GetNumDays():
    numDays = input(
        " How many days did you serviced haircuts this month(Half, Whole)? \t   "
    )
    return numDays


# Prompt the amount of tips recieved for the month and Get the user response
def GetTotalTips():
    totalTIPS = int(
        input(
            " How much tips did you recieve this month(any number ≥ 0)? \t   "
        )
    )
    return totalTIPS


# Calculate the total number of haircuts for the month
def CalTotalHair(numHAIR, numDays):
    # This function calculates the total number of haircuts for the month
    # Input:  numHAIR, numDays
    # Output: totalPay

    # Declare variables:
    # numHAIR, numDays, totalTIPS,  hairCost, commPCT, totalHAIR, mthSal, totalPay

    # Initialize variables:
    hairCost = 84
    commPCT = 75

    Few = 4  # Few is simply a small number
    Several = 8  # Several is simply a medium number(neither small nor large)
    Many = 12  # Many is simply a large number

    Half = 15  # Half is simply half the month(15 days out the month)
    Whole = (
        30  # Whole is simply the whole month(every single day of the month)
    )

    # Calculate the few number of haircuts for the month
    if numHAIR == "Few":
        if numDays == "Half":
            totalHAIR = Half * Few
        elif numDays == "Whole":
            totalHAIR = Whole * Few

    # Calculate the several number of haircuts for the month
    if numHAIR == "Several":
        if numDays == "Half":
            totalHAIR = Half * Several
        elif numDays == "Whole":
            totalHAIR = Whole * Several

    # Calculate the many number of haircuts for the month
    if numHAIR == "Many":
        if numDays == "Half":
            totalHAIR = Half * Many
        elif numDays == "Whole":
            totalHAIR = Whole * Many

    return totalHAIR


# Calculate the monthly salary
def CalMthSal(totalHAIR):
    # This function calculates the monthly salary
    # input:  totalHAIR, commPCT, hairCost
    # Output: mthSal
    # Initialize variables:
    hairCost = 84
    commPCT = 75
    mthSal = totalHAIR * (commPCT / 100) * hairCost

    return mthSal


# Calculate the total pay for the month
def CalBarberService(mthSal, totalTIPS):
    # This function calculates the total pay for the month
    # input:  mthSal, totalTIPS
    # Output: totalPay
    # Initialize variables:

    # Change made by Jonathan Weaver
    totalPay = mthSal + totalTIPS
    average_pay_per_day = totalPay / WORKING_DAYS_IN_A_MONTH

    return average_pay_per_day


# Display the barber output
def DisplayBarberService(totalHAIR, mthSal, average_pay_per_day):
    # This function displays the total number of haircuts for the month
    # Input: totalHAIR, mthSal, totalPay
    # Output: None

    print(
        " the total number of haircuts for the month is:          ", totalHAIR
    )
    print(" the monthly salary is:                                 $", mthSal)

    # Change made by Jonathan Weaver
    # Print out the average pay per day instead of total
    print(
        " The Total average pay for the month is:                        $",
        average_pay_per_day,
    )


# Display the shop output
def DisplayShopService(totalShopHAIR, mthShopSal, totalShopPay):
    # This function displays the total number of shop haircuts for the month and your name, course/section, date
    # Input: totalShopHAIR, mthShopSal, totalShopPay
    # Output: None

    print(
        "\n the total number of shop haircuts for the month is:   ",
        totalShopHAIR,
    )
    print(
        " the total monthly shop salary is:                      $", mthShopSal
    )
    print(
        " The Total Shop pay for the month is:                   $",
        totalShopPay,
    )
    print("\n------- Name:     Eric Alexander II ----------")
    print("CMIS 102/6986              Date: June 27, 2022")
    print("modified for If statements Date: July 03, 2022")
    print("modified for Functions     Date: July 09, 2022")
    print("modified for Loops         Date: July 15, 2022")
    print("----------------------------------------------")


# Display all functions
def main():
    # Display Welcome message
    WelcomeMessage()

    totalHAIRShop = 0
    mthSalShop = 0
    totalPayShop = 0
    moreProBarbers = True

    while moreProBarbers:
        # Prompt the user for number of haircuts in a single shift and Get the user response
        numHAIR = GetNumHair()

        # Prompt the user for number of days hair cuts is serviced per month and Get the user response
        numDays = GetNumDays()

        # Prompt the amount of tips recieved for the month and Get the user response
        totalTIPS = GetTotalTips()

        # Calculate the total number of haircuts for the month
        totalHAIR = CalTotalHair(numHAIR, numDays)

        # Calculate the monthly salary
        mthSal = CalMthSal(totalHAIR)

        # Calculate the average number of haircuts for the month
        average_pay_per_day = CalBarberService(mthSal, totalTIPS)

        # Display the barber output
        DisplayBarberService(totalHAIR, mthSal, average_pay_per_day)

        # Accumulate Shop Totals
        totalHAIRShop = totalHAIRShop + totalHAIR
        mthSalShop = mthSalShop + mthSal
        totalPayShop = totalPayShop + average_pay_per_day

        # Prompt another professional barber
        babble = input("\n Another professional barber ?  [Y/N]:\t")
        if babble.upper() != "Y":
            moreProBarbers = False

        # Display the shop output
        DisplayShopService(totalHAIRShop, mthSalShop, totalPayShop)


# Execute
main()
