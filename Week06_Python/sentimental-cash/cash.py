from cs50 import get_float


def main():
    # Get user input as the change owed, in dollars
    while True:
        dollars = get_float("Change owed: ")
        if dollars >= 0:
            break

    # Convert dollars to cents
    cents = round(dollars * 100)

    # Calculate how many quarters you should give customer
    quarters = calculate_quarters(cents)
    # Subtract the value of those quarters from cents
    cents -= quarters * 25

    # Calculate how many dimes you should give customer
    dimes = calculate_dimes(cents)
    # Subtract the value of those dimes from remaining cents
    cents -= dimes * 10

    # Calculate how many nickels you should give customer
    nickels = calculate_nickels(cents)
    # Subtract the value of those nickels from remaining cents
    cents -= nickels * 5

    # Calculate how many pennies you should give customer
    pennies = calculate_pennies(cents)
    # Subtract the value of those pennies from remaining cents
    cents -= pennies

    # Sum the number of quarters, dimes, nickels, and pennies used
    coins = quarters + dimes + nickels + pennies

    # Print that sum
    print(coins)


def calculate_quarters(cents):
    quarters = 0
    while cents >= 25:
        quarters += 1
        cents -= 25
    return quarters


def calculate_dimes(cents):
    dimes = 0
    while cents >= 10:
        dimes += 1
        cents -= 10
    return dimes


def calculate_nickels(cents):
    nickels = 0
    while cents >= 5:
        nickels += 1
        cents -= 5
    return nickels


def calculate_pennies(cents):
    pennies = 0
    while cents >= 1:
        pennies += 1
        cents -= 1
    return pennies


main()
