# Gerald Parker

# CMIS 102/6986

# July 29th, 2022

# program calculates hours worked information and paycheck total

# Welcome statement


print("Please enter hours for the week.")

# -----------------------------------------------------------------


# empty variable


hours = []

# ----------------------------------------------------------------------


# loop for user input on amount of hours


hoursin = eval(
    input("Please enter how many hours you worked (Enter any -1 to exit): ")
)

while hoursin != -1:

    hours.append(hoursin)

    hoursin = hoursin + 1

    hoursin = eval(
        input("And next day how many hours (Enter any -1 to exit): ")
    )

# --------------------------------------------------------------------------


# print sum, average, max, and min of hours.

# also print paycheck total


print("Total hours worked this week:", sum(hours))

print("Average hours worked per week:", sum(hours) / len(hours))

print("Most hours worked this week:", max(hours))

print("Least amount of hours worked this week:", min(hours))

print("Your paycheck is:", sum(hours) * 31.00)

# Modification made by Jonathan Weaver
# Modify the code to get the bonus you get for the hours worked
print("Your bonus for the hours worked per week is:", (sum(hours) * 31.00 / 2))

# --------------------------------------------------------------------------
