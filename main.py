"""
COMP 1500 Integration Project | Football tools
"""
__author__ = "Ethan Hammond"


# Sprint #1 Requirements

def sprint1():
    """
    Filling requirement for the first sprint project inspection
    """
    # Simple IO
    # the print() function including a greeting / introduction to the user
    # formatting print() output with end= arguments
    print("The best football team is the", end=" Jacksonville Jaguars!\n")
    # formatting print() output with sep= arguments
    print("The Super Bowl is on 2", "13", "2022", sep='-')
    # the input() function
    bengals_score = input("How many points do you think the Bengals will score?: ")
    rams_score = input("How many points do you think the Rams will score?: ")

    # Basic Calculations

    # Numeric Operators (use and include a comment explaining)
    # ** (to the power of)
    print(bengals_score, "to the power of", rams_score, "=", int(bengals_score) ** int(rams_score))
    # *  (multiplication)
    print(bengals_score, "times", rams_score, "=", int(bengals_score) * int(rams_score))
    # /  (Division)
    print(bengals_score, "divided by", rams_score, "=", int(bengals_score) / int(rams_score))
    # %  (Division remainder)
    print("The remainder of", bengals_score, "divided by", rams_score, "=", int(bengals_score) % int(rams_score))
    # // (Return largest value closest to input)
    print("The floor of", bengals_score, "divided by", rams_score, "=", int(bengals_score) // int(rams_score))
    # +  (Addition)
    print(bengals_score, "+", rams_score, "=", int(bengals_score) + int(rams_score))
    # -  (Subtraction)
    print(bengals_score, "-", rams_score, "=", int(bengals_score) - int(rams_score))

    # String Operators (use and include a comment explaining)
    favorite_team = input("What is your favorite football team?: ")
    # * (prints string amount of times it is multiplied by)
    print(favorite_team * 10)
    # + (Adds on after + to the end of what is before the +)
    print(favorite_team, "beat the Tennessee Titans by " + bengals_score + " points")


# Sprint 2
def square(whole_num):
    """
    squares a number passed ass param whole_num
    :param whole_num:
    """
    whole_num * whole_num


def sprint2():
    """
    Filling requirement for the second sprint project inspection
    """
    # shortcut operators
    number_a = int(input("Please input a whole number: "))
    number_b = int(input("Please input a whole number again: "))

    # +=
    total = number_a
    total += number_b
    print(number_a, '+', number_b, "=", total)

    # -=
    total = number_a
    total -= number_b
    print(number_a, '-', number_b, "=", total)

    # *=
    total = number_a
    total *= number_b
    print(number_a, '*', number_b, "=", total)

    # /=
    total = number_a
    total /= number_b
    print(number_a, '*', number_b, "=", total)

    # relational operators

    # ==
    if number_a == number_b:
        print("The numbers are the same!")

    # !=
    if number_a != number_b:
        print("The numbers are not the same!")

    # >
    if number_a > number_b:
        print("The first number is larger than the second")

    # boolean operators

    number_c = int(input("Please input a third whole number: "))
    number_d = int(input("Please input a fourth whole number: "))

    # and
    if number_a > number_b and number_c > number_d:
        print("Both first numbers in each set are greater than the 2nd")
    # or
    if number_a > number_b or number_c > number_d:
        print("One of the first numbers in the two sets is greater than the 2nd")

    # not

    if not (number_a > number_b):
        print("The 2nd number is larger than the 1st number")

    # while
    # in menu function

    # for
    # in
    # range

    number_x = int(input("please input a whole number"))

    for x in range(number_x):
        print("HeHeHeHaw")

    # function def
    # main, sprint1 and 2

    # func with parameters

    print(number_x, "squared =", square(number_x))


# Cool Stuff
def fun_stuff():
    """
    Football winning odds calculator
    """
    # Calculate the odds of a team winning a game

    # difference in score between two teams (current game)

    odds = 0.50
    score_differential = input("What is the current score differential?")

    # if our team is winning
    if int(score_differential) > 0:
        # increase odds by the number of touchdowns and field goals divided by 50
        odds += ((int(score_differential) / 7) + ((int(score_differential) % 7) / 3)) / 50
        # if our team is losing
    elif int(score_differential) < 0:
        # decrease odds by the number of touchdowns and field goals divided by 50
        odds -= ((-(int(score_differential)) / 7) + ((-(int(score_differential)) % 7) / 3)) / 50

    print(odds)


#   Menu
def print_menu():
    """
    prints out selection options for pages the user can select and handles selections with error handling
    """
    print("1. Sprint 1")
    print("2. Sprint 2")
    print("3. Fun thing")


valid_choice = False

while not valid_choice:
    print("Welcome to my Integration Project!")
    print_menu()
    choice = int(input("Select which spring you are section you are looking for!"))

    if choice == 1:
        sprint1()
        valid_choice = True
    elif choice == 2:
        sprint2()
        valid_choice = True
    elif choice == 3:
        fun_stuff()
        valid_choice = True
    else:
        print("Invalid selection - please try again")
