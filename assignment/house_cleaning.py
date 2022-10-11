"""
House cleaning cost.

Calculate the cost of house cleaning based on :-
    - The number of rooms in the house.
    - The type of cleaning that the customer requires, whose
      cost is based on whether the house has a small, medium or 
      large number of rooms.
"""

# A small house is a house with two or less rooms
SMALL_NUMBER_OF_ROOMS = 2

# A medium house is a house with more than two rooms but less or equal to 4 rooms
MEDIUM_NUMBER_OF_ROOMS = 4

# A large house is a house with greater or equal to 6 rooms
LARGE_NUMBER_OF_ROOMS = 6

FLOORS = "FLOORS"
WINDOWS = "WINDOWS"
BATHROOMS = "BATHROOMS"

# The types of cleaning that we offer
TYPES_OF_CLEANING = [FLOORS, WINDOWS, BATHROOMS]

# This represents our price list, with the prices of each type of cleaning
# based on the number of rooms that you have in your house
PRICE_LIST = {
    "SMALL": {
        FLOORS: 200,
        WINDOWS: 250,
        BATHROOMS: 300,
    },
    "MEDIUM": {
        FLOORS: 400,
        WINDOWS: 450,
        BATHROOMS: 500,
    },
    "LARGE": {
        FLOORS: 600,
        WINDOWS: 650,
        BATHROOMS: 700,
    },
}


def main():
    """Calculate the cost of cleaning a house."""
    # Prompt the user to enter their number of houses, and type of cleaning
    print("\nLet us clean your house.")
    number_of_rooms = int(
        input("How many rooms do you want cleaned? ")
    )
    print(
        "\nSelect the type of cleaning that you require from the options below"
    )
    print("1. FLOORS\n2. WINDOWS\n3. BATHROOMS")
    type_of_cleaning = input(
        "What type of cleaning do you want from us? "
    )

    # Validate the type of cleaing entered is part of what we offer
    type_of_cleaning = type_of_cleaning.upper()
    if type_of_cleaning not in TYPES_OF_CLEANING:
        print("\nSorry! We dont offer that type of cleaning.")
        return

    # Calculte the cost of a small number of rooms
    if number_of_rooms <= SMALL_NUMBER_OF_ROOMS:
        price = PRICE_LIST["SMALL"][type_of_cleaning]
        total_cost = price * number_of_rooms
        print(
            f"\nThe total cost for cleaning your house is {total_cost}"
        )
        return

    # Calculte the cost of a medium number of rooms
    if number_of_rooms > SMALL_NUMBER_OF_ROOMS and number_of_rooms <= MEDIUM_NUMBER_OF_ROOMS:
        price = PRICE_LIST["MEDIUM"][type_of_cleaning]
        total_cost = price * number_of_rooms
        print(
            f"\nThe total cost for cleaning your house is {total_cost}"
        )
        return

    # Calculte the cost of a large number of rooms
    if number_of_rooms >= LARGE_NUMBER_OF_ROOMS:
        price = PRICE_LIST["LARGE"][type_of_cleaning]
        total_cost = price * number_of_rooms
        print(
            f"\nThe total cost for cleaning your house is {total_cost}"
        )
        return


if __name__ == "__main__":
    main()
