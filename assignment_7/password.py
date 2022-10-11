"""
Password checker.

Python program to determine whether a password exactly 
meets the following requirements for a secure password:
    1. The length of the password must greater than some minimum length and less than some maximum
    2. It must not include any spaces
    3. It must contain at least one digit
    4. It must contain at least one alphabetic character
"""

# A strong password should have a minimum of 7 characters
MINIMUM_LENGTH = 7

# A strong password should have a maximum of 20 characters
MAXIMUM_LENGTH = 20


def check_password_length(password):
    """Check the minimum and maximum password length."""
    length = len(password)
    return (
        False if length < MINIMUM_LENGTH or length > MAXIMUM_LENGTH else True
    )


def check_required_characters(password):
    """Check the password has the required number of characters/digits."""
    for each in password:
        is_all_alpha = each.isalpha()
        if is_all_alpha is False:
            return True
    return False


def check_space(password):
    """Check if the password has a space."""
    return False if " " in password else True


def main():
    """Python program entry point."""
    password = str(input("\nEnter your strong password: "))
    length_check = check_password_length(password)
    if length_check is False:
        print(
            f"\nPassword should have at least {MINIMUM_LENGTH} characters and at most {MAXIMUM_LENGTH} characters\n"
        )
        return

    character_check = check_required_characters(password)
    if character_check is False:
        print(
            f"\nPassword should contain atleast one alphabetic character or one number\n"
        )
        return

    space_check = check_space(password)
    if space_check is False:
        print(f"\nPassword should not contain a space\n")
        return

    print("\nYour password is valid\n")


if __name__ == "__main__":
    main()
