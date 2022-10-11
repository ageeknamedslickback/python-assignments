"""
This program computes the weekly pay for a paper carrier. The user will input the following fields
    - number of papers on the route
    - number of days the papers are delivered per week
    - amount of tips received for the week

The predefined values are:
    - Cost of each newspaper is set to $5
    - Commission = 25%
    
The program will then return/ print the following fields after calculations:
    - the total number of papers delivered for the week
    - the weekly salary
    - the tips for the week 
    - the total pay for the week

"""


def main():
    newspaper_cost = 5.0
    commission_rate = 0.25

    # Prompt user for the number of papers on route
    number_of_papers_onroute = int(input("Enter the number of papers on the route: "))

    # Prompt user for the number of papers is delivered per week
    number_of_days_papers_is_delivered = int(
        input("Enter the number of days the paper is delivered per week: ")
    )

    # Prompt user for the number of tips received for the week
    tips_amount = int(input("Enter the amount of tips received for the week: "))

    total_papers_per_week = (
        number_of_papers_onroute * number_of_days_papers_is_delivered
    )
    weekly_salary = total_papers_per_week * newspaper_cost * commission_rate
    total_pay = weekly_salary + tips_amount

    print(
        f"\nThe total number of papers delivered for the week is {str(total_papers_per_week)} papers."
    )
    print(
        f"Your weekly salary is ${str(weekly_salary)}. This total is calculated from a newspaper cost of $5 and a commision rate of 25%"
    )
    print(f"The total amount collected in tips is ${str(tips_amount)}")
    print(f"The total pay for the week is ${str(total_pay)}")


if __name__ == "__main__":
    main()
