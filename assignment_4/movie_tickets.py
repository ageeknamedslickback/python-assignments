"""
Comupute the cost of a movie ticket.

The computation of the price of the movie ticket is based
on the movie selected and the number of people that
are going to catch the blockbuster movie.
"""
# The movies that are offered in the cinema and their price
DOCTOR_STRANGE_IN_THE_MULTIVERSE_OF_MADNESS = 100
THOR_LOVE_AND_THUNDER = 200
BLACK_PANTHER_WAKANDA_FOREVER = 300


def movie_cost(movie, number_of_people):
    """Compute the cost of watching a movie."""
    movie_cost = 0

    # Calculate the cost of a movie based on the number of people
    # going to watch it.
    if movie == 1:
        movie_cost = (
            DOCTOR_STRANGE_IN_THE_MULTIVERSE_OF_MADNESS * number_of_people
        )
    elif movie == 2:
        movie_cost = THOR_LOVE_AND_THUNDER * number_of_people
    elif movie == 3:
        movie_cost = BLACK_PANTHER_WAKANDA_FOREVER * number_of_people
    else:
        movie_cost = None

    return movie_cost


def main():
    """Calculate the cost of cleaning a house."""
    # Prompt the user to select a movie and the number of people
    # going to watch the movie
    print("\nWelcome to the Marvel cinematic fun.")
    print(
        "1. Doctor Strange in the Multiverse of Madness\n"
        "2. Thor: Love and Thunder\n"
        "3. Black Panther: Wakanda Forever"
    )
    movie = int(input("What movie do you want to watch today (1,2 or 3)? "))
    number_of_people = int(input("How many people are watching the movie? "))

    # Validate the number of people should be greater or equal to one
    if number_of_people < 1:
        print("\nSorry! Number of people must be one or many")
        return

    # Compute the cost of cleaning the house
    cost = movie_cost(movie, number_of_people)
    if cost is None:
        print("\nSorry! Please pick a movie by entering 1, 2 or 3.")
    else:
        print(f"\nThe total cost for your movie is {cost}")


if __name__ == "__main__":
    main()
