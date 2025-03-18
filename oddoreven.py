"""Program evaluates number input for odd or even"""
# plan:
# prompt user for input,
# evaluate input % 2 == 0,
# return odd or even
# ask to take another number or exit


def odd_or_even(num):
    """evaluates and returns if num is odd or even"""
    # num: the user's number

    if num % 2 == 0:
        return True
    else:
        return False


def main():
    """the main function"""
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


if __name__ == "__main__":
    main()
