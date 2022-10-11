"""
Loan calculator.

This program computes the total amount a customer
has to pay back for their loan amount, given their
preferred repayment period. 

Female customers have a good loan track record, 
and thus they get lower interest rates as compared 
to their male counter parts.
"""

MALE_INTEREST_RATE = 5.6
FEMALE_INTEREST_RATE = 3.6


def compute_loan(interest_rate, loan_amount, period):
    """Peform the actual loan computation."""
    monthly_interest_earned = (interest_rate / 100) * loan_amount
    total_interest_earned = monthly_interest_earned * period
    payable_loan_amount = loan_amount + total_interest_earned
    print(
        f"\nTotal payable amount after {period} month is {payable_loan_amount}"
    )


def main():
    """Compute the payable loan amount."""
    print("\nWelcome to your personal Loan Calculator.\n")
    gender = input("What is your gender (male/female): \n")
    loan = float(input("\nWhat loan amount are you interested in?\n"))
    period = int(
        input(
            "\nHow many months would you like to pay back the loan?\n"
        )
    )

    if gender == "female":
        compute_loan(FEMALE_INTEREST_RATE, loan, period)

    elif gender == "male":
        compute_loan(MALE_INTEREST_RATE, loan, period)

    else:
        print("\nGender should either be male or female")


if __name__ == "__main__":
    main()
