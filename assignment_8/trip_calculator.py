"""
Road Trip Data.

Collect road trip data and calculate the various costs involved in a road trip
given the number of people and days spent.
The program calculates:
    1. The total cost per category (food/gas)
    2. The total cost of the trip
    3. The total cost per person for the whole trip
"""

# The unit cost of food per person for each day
UNIT_COST_OF_FOOD_PER_PERSON = 147

# The unint cost of gas per day
UNIT_COST_OF_GAS_PER_DAY = 169


def total_food_and_gas_cost(people, days):
    """Calculate the total cost of each category."""
    # Total cost of food for each person
    food_cost_list = []
    for _ in range(people):
        food_cost_list.append(UNIT_COST_OF_FOOD_PER_PERSON * days)
    total_food_cost = sum(food_cost_list)

    # Total gas cost for the days
    gas_cost_list = []
    for _ in range(days):
        gas_cost_list.append(UNIT_COST_OF_GAS_PER_DAY)
    total_gas_cost = sum(gas_cost_list)

    return total_food_cost, total_gas_cost


def total_cost_of_trip(total_food_cost, total_gas_cost):
    """Calculate the total cost of the trip."""
    return total_food_cost + total_gas_cost


def each_person_share_of_the_total_cost(total_cost, people):
    """Calculate each person's share of the total cost."""
    return total_cost / people


def main():
    """Python program entrypoint."""
    print(
        "Get the cost of your trip with your friends.\n"
        "=============================================\n"
    )
    people = int(input("How many people are on the trip? "))
    days = int(input("How many days will the trip be? "))

    total_food_cost, total_gas_cost = total_food_and_gas_cost(people, days)

    print("\nCalculating . . .\n")
    print(f"Your total cost for Food is ${total_food_cost}")
    print(f"Your total cost for Gas is ${total_gas_cost}\n")

    total_trip_cost = total_cost_of_trip(total_food_cost, total_gas_cost)
    print(f"Your total cost for your trip is ${total_trip_cost}")

    cost_per_person = each_person_share_of_the_total_cost(
        total_trip_cost, people
    )
    print(
        f"Your total cost for per person your trip is ${round(float(cost_per_person), 2)}\n"
    )


if __name__ == "__main__":
    main()
