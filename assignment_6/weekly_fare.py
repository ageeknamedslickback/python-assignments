"""
Weekly Fare Calculator.

Calculate the total fare amount a person uses to
commute in a week (7 days)
"""
import sys


def sum_weekly_fare():
    """Get the sum of the total weekly fare."""
    # Keep a count of the number of days. They should not exceed 7
    days_count = 0

    # List(store) the daily fare amounts for summation
    weekly_fare = []

    # Keep asking the user input till the days count reach 7
    while days_count < 7:
        inp = input(
            "\nEnter the amount of fare you used on this day (Enter q to quit): "
        )

        # Exit the calculator if the user enters "q" or "Q"
        if inp == "q" or inp == "Q":
            print("Exiting the calculator")
            sys.exit()

        # Add the inputted fare to the list and increament the days count
        weekly_fare.append(float(inp))
        days_count += 1

    # Sum the daily fares in the list and return the summation
    return sum(weekly_fare)


def main():
    """Entry point to the program"""
    weekly_fare = sum_weekly_fare()
    print(
        f"\nYour commute fare expenditure for the last 7 days is {weekly_fare}"
    )


if __name__ == "__main__":
    main()
