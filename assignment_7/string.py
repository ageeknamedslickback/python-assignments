"""Random string game."""

MAGIC_CHARACTER = "A"
FIRST_INITIAL = "J"
SECOND_INITIAL = "W"

def main():
    """Python program entry point."""
    print(
        "Let's play a game. Enter the first word that comes in your mind ;)\n"
        "==================================================================\n"
        )
    word = str(input("What's the first word that comes in your mind? "))
    captialized_word = word.capitalize()
    if MAGIC_CHARACTER in captialized_word:
        print(f"\nYay! Your word contains the magic character {MAGIC_CHARACTER}")

    if FIRST_INITIAL in captialized_word or SECOND_INITIAL in captialized_word:
        print(f"How lucky! Your word contains one or both of my initials")

    print(f"Your word has {captialized_word.count(MAGIC_CHARACTER)} magic characters `{MAGIC_CHARACTER}`\n")


if __name__ == "__main__":
    main()