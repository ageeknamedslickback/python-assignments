"""
Weighted average.

Calculate the weighted average for each student
and determine the student with the highest average.

We calculate the weighted average of the student based
on their quiz, discussion and programming assignment grades.
For each, we have assigned a weight that we use to get the
weighted average, ie weight * grade which we then sum to get 
the best student
"""

# Quiz weight value is specified as .10
QUIZ_WEIGHT = 0.10

# Discussion weight value is specified as .40
DISCUSSION_WEIGHT = 0.30

# Programming assignment weight value is specified as .60
PROGRAMMING_WEIGHT = 0.60

# Class list with the name of the existing four students
STUDENTS = ["Alice", "Bob", "Jane", "John"]


def get_best_student_with_the_highest_grade(student_name):
    """Get the best student with the highest weighted average."""
    # Assign a default highest grade and a best student name
    highest_grade = 0.0
    best_student = ""

    print(f"\n\nProvide the following information for {student_name}")
    print("=============================================\n")

    # For each student, prompt the user to enter their grade
    # for each of quiz, discussion and programming assignment
    quiz_grade = float(input(f"What is {student_name}'s quiz grade? "))
    discussion_grade = float(
        input(f"What is {student_name}'s discussion grade? ")
    )
    programming_grade = float(
        input(f"What is {student_name}'s programming assignment grade? ")
    )

    # Calculate the weighted average of each student
    weighted_average = (
        (quiz_grade * QUIZ_WEIGHT)
        + (discussion_grade * DISCUSSION_WEIGHT)
        + (programming_grade * PROGRAMMING_WEIGHT)
    )

    # Check for the highest grade and the student with the highest grade
    if weighted_average > highest_grade:
        highest_grade = weighted_average
        best_student = student_name

    return best_student, highest_grade


def main():
    """Computed the weighted average of students and return the highest."""
    print(
        "\nWelcome to your class grade weighted average calculator\n"
        "==========================================================\n"
        "We will require the following from you:\n"
        "\t1. The names of your four (4) students\n"
        "\t2. The students' quiz, discussion and programming grades\n"
    )

    # The program accepts a list of 4 students
    for _ in range(0, 4):
        student_name = str(input("\nWhat is the name of your student? "))

        # If the student name provided is not in the students list stop execution
        if student_name.capitalize() not in STUDENTS:
            print(
                f"\nThe student {student_name} does not belong to this class"
            )
            return

        best_student, highest_grade = get_best_student_with_the_highest_grade(
            student_name=student_name
        )

    print(
        f"\n\n{best_student} is the student with the highest grade of {highest_grade}"
    )


if __name__ == "__main__":
    main()
