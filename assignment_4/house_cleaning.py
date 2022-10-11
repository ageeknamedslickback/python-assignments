"""
House or yard cleaning cost.

Calculate the cost of house cleaning based on :-
    - The number of rooms in the house.
    - The type of cleaning that the customer requires, whose
      cost is based on whether the house has a small, medium or 
      large number of rooms.

Caluclate the cost of yard cleaning services such as an based on:-
    - Mowing, whose cost depends upon the square footage of the yard
    - Edging, whose cost depends upon the linear footage of the yard's edges
    - Shrub prunning, whose cost depends upon the number of shrubs
"""

# A small house is a house with two or less rooms
SMALL_NUMBER_OF_ROOMS = 2

# A medium house is a house with more than two rooms but less or equal to 4 rooms
MEDIUM_NUMBER_OF_ROOMS = 4

# A large house is a house with greater or equal to 6 rooms
LARGE_NUMBER_OF_ROOMS = 6

LIGHT = "LIGHT"
COMPLETE = "COMPLETE"

# The types of house cleaning cleaning that we offer
TYPES_OF_HOUSE_CLEANING = [LIGHT, COMPLETE]

# This represents our price list, with the prices of each type of cleaning
# based on the number of rooms that you have in your house
PRICE_LIST = {
    "SMALL": {
        LIGHT: 200,
        COMPLETE: 250,
    },
    "MEDIUM": {
        LIGHT: 400,
        COMPLETE: 450,
    },
    "LARGE": {
        LIGHT: 600,
        COMPLETE: 650,
    },
}

# The different yard services being offered
MOWING = "MOWING"
EDGING = "EDGING"
PRUNNING = "PRUNNING"

# Represents all the types of yard services we offer
TYPES_OF_YARD_SERVICES = [MOWING, EDGING, PRUNNING]

# The different unit price for the yard cleaning services
MOWING_PRICE_PER_SQ_FOOTAGE = 178
EDGING_PRICE_PER_LINEAR_FOOTAGE = 102
SHRUBBING_PRICE_PER_SHRUB = 13

# Aggregated yard cleaning services price list
YARD_PRICE_LIST = {
    MOWING: MOWING_PRICE_PER_SQ_FOOTAGE,
    EDGING: EDGING_PRICE_PER_LINEAR_FOOTAGE,
    PRUNNING: SHRUBBING_PRICE_PER_SHRUB,
}

# The different types of services that we offer (Yard and House services)
YARD_SERVICES = "YARD"
HOUSE_SERVICES = "HOUSE"

# Seniors from age 65 and above get a fixed dollar discount on the cleaning services of their choice
SENIORS_DISCOUNT_FIXED_AMOUNT = 200
SENIORS_AGE = 65


def house_cleaning_cost(number_of_rooms, type_of_cleaning):
    """Compute the cost of cleaning a house based on the size and type of cleaning."""
    total_cost = 0

    # Validate the type of cleaing entered is part of what we offer
    type_of_cleaning = type_of_cleaning.upper()
    if type_of_cleaning not in TYPES_OF_HOUSE_CLEANING:
        return None

    # Calculate the cost of a small number of rooms
    if number_of_rooms <= SMALL_NUMBER_OF_ROOMS:
        price = PRICE_LIST["SMALL"][type_of_cleaning]
        total_cost = price * number_of_rooms

    # Calculate the cost of a medium number of rooms
    if (
        number_of_rooms > SMALL_NUMBER_OF_ROOMS
        and number_of_rooms <= MEDIUM_NUMBER_OF_ROOMS
    ):
        price = PRICE_LIST["MEDIUM"][type_of_cleaning]
        total_cost = price * number_of_rooms

    # Calculate the cost of a large number of rooms
    if number_of_rooms >= LARGE_NUMBER_OF_ROOMS:
        price = PRICE_LIST["LARGE"][type_of_cleaning]
        total_cost = price * number_of_rooms

    return total_cost


def yard_cleaning_cost(type_of_yard_cleaning, units):
    """Compute the total cost of cleaning a yard."""
    # Validate the type of yard cleaning required
    type_of_yard_cleaning = type_of_yard_cleaning.upper()
    if type_of_yard_cleaning not in TYPES_OF_YARD_SERVICES:
        return None

    return YARD_PRICE_LIST[type_of_yard_cleaning] * units


def calculate_seniors_discount(total_cost):
    """Calculates the total cost of cleaning services for seniors using their discount."""
    return total_cost - SENIORS_DISCOUNT_FIXED_AMOUNT


def main():
    """Calculate the cost of cleaning a house."""
    type_of_cleaning = ""

    # Prompt the user to selcet their type of cleaning
    while True:
        print(
            "\nWelcome to our re-defined house and yard cleaning services\n"
            "==========================================================\n\n"
            "Please select the where you want the cleaning services to be done:\n "
            f"1. {HOUSE_SERVICES}\n 2. {YARD_SERVICES}\n"
        )
        type_of_cleaning_inp = str(input("")).upper()
        if (
            type_of_cleaning_inp == HOUSE_SERVICES
            or type_of_cleaning_inp == YARD_SERVICES
        ):
            type_of_cleaning = type_of_cleaning_inp
            break

    # Handle house cleaning services
    if type_of_cleaning == HOUSE_SERVICES:
        # Prompt the user to enter their number of houses, and type of cleaning
        print("\nLet us clean your house.")
        number_of_rooms = int(input("How many rooms do you want cleaned? "))
        print(
            "\nSelect the type of cleaning that you require from the options below"
        )
        print(f"1. {LIGHT}\n2. {COMPLETE}\n")
        type_of_cleaning = input("What type of cleaning do you want from us? ")

        # Collect the age of the user
        age = int(input("One final question :). How old are you today? "))

        # Compute the cost of cleaning the house
        total_cost = house_cleaning_cost(number_of_rooms, type_of_cleaning)
        if total_cost is None:
            print("\nSorry! We don't offer that type of cleaning.")
        else:
            if age >= SENIORS_AGE:
                total_cost = calculate_seniors_discount(total_cost)
            print(
                f"\nThe total cost for cleaning your house is {total_cost}. "
                "Thank You for choosing us."
            )

    # Handle yard cleaning services
    if type_of_cleaning == YARD_SERVICES:
        # Prompt the user to select the type of yard services they require
        print(
            "\nLet us clean your yard.\n"
            "Select the type of yard cleaning that you require\n"
            f"1. {MOWING}2. {EDGING}3. {PRUNNING}\n"
        )
        type_of_yard_cleaning = str(input("")).upper()
        print(
            "Enter the unit of work to be done, that is, "
            "the square footage for mowing, "
            "linear footage of yard's edges for edging or "
            "number of shrubs to be prunned: \n"
        )
        unit = int(input(""))
        age = int(input("One final question :). How old are you today? "))

        # Calculate the total cost of yard cleaning based on the yard services selected
        total_cost = yard_cleaning_cost(type_of_yard_cleaning, unit)
        if total_cost is None:
            print("\nSorry! We don't offer that type of cleaning.")
        else:
            if age >= SENIORS_AGE:
                total_cost = calculate_seniors_discount(total_cost)
            print(
                f"\nThe total cost for cleaning your yard is {total_cost}. "
                "Thank You for choosing us."
            )


if __name__ == "__main__":
    main()
