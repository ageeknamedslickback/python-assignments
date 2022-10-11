"""
Play a game with age. Where will you be in 10 years.
Use three loops to modify the array and print the output
"""

# The minimum number of elements the user can input
MINIMUM_ELEMENTS = 5

# Single list of manipulatable ages
AGES = []


def main():
    """Python program entrypoint"""
    elements = 0
    while elements < MINIMUM_ELEMENTS:
        input_age = int(
            input("\nEnter a random age that comes into your mind: ")
        )
        AGES.append(input_age)
        elements += 1

    for each in range(len(AGES)):
        # Add 10 years to each age
        AGES[each] += 10

    print(
        "\nGive us a moment we verify what the ages will look like in 10 years\n"
        "===================================================================\n"
    )
    for modified_age in AGES:
        # Display the modified array
        print(f"{modified_age}\n")


if __name__ == "__main__":
    main()
