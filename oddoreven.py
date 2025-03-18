"""Program evaluates number input for odd or even"""
# plan:
# prompt user for input,
# evaluate input % 2 == 0,
# return odd or even
# ask to take another number or exit

import sys


def odd_or_even(num):
    """evaluates and returns if num is odd or even"""
    # num: the user's number

    if num % 2 == 0:
        return True
    else:
        return False


def go_again():
    """function checks if user wants to keep going or exit"""
    while True:
        choice = input(
            "\nDo you want to check another number or stop here? (yes/no)\n-: ").strip().lower()

        if choice == "yes":
            break
        elif choice == "no":
            sys.exit()
        else:
            print("Please enter 'yes' or 'no'.\n")


def main():
    """the main function"""
    while True:
        while True:
            try:
                num = int(
                    input("\nPlease enter which number I should check for odd or even!\n-: "))
                break
            except ValueError:
                print("Invalid input! Please enter a number")

        if odd_or_even(num):
            print("Even!")
        else:
            print("Odd!")

        go_again()


if __name__ == "__main__":
    main()
