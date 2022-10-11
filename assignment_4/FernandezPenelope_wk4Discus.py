# Penelope Fernandez
# CMIS 102/6986.
# 7/8/2022
# Week 4 Discussion


# Calculate the area of a rectangle:

# The user will prompt the lenght and width of a rectagle

print("Please, provide the lenght of the two sides of a rectangle, \n ")

side1 = int(input("Enter the length of one side: "))
side2 = int(input("Enter the length of the second side: "))


def sum_of_rectangle_length_and_width(side1, side2):
    # Instead of calculating the area of the rectangle, we are now
    # computing the sum of the length and width of the rectangle
    sum = side1 + side2
    return sum


print(
    "\n The sum of the rectanlge is ",
    sum_of_rectangle_length_and_width(side1, side2),
    " meters",
)
