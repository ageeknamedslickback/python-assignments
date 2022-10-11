"""
Compute the time taken to get to your destination.

Given your current speed and the distance to be covered, 
this program calculates the total time that you will take to
arrive at your destination. It goes ahead and adds an hour
give or take, to account for anything that might happen along the way.

It:
    - Accepts at least two inputs - distance and speed.
    - Calculates the time taken to arrive to destination.
    - Output the time on the prompt.
"""


# Additional hour(s) to account for any inconviniences
ADDITIONAL_HOURS = 1


def main():
    """Compute the time taken to reach your destination."""
    distance = input("Enter the total distnace you are going to cover(km)\n")
    speed = input("Enter your average speed(km/h)\n")

    time_taken = float(distance) / float(speed)
    approximate_time_taken = time_taken + ADDITIONAL_HOURS

    print(
        f"\nYou will approximately take {approximate_time_taken:.2f} "
        "hours to reach your destination\n"
    )


if __name__ == "__main__":
    main()
