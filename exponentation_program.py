#customer requests
#requests:
#1- get two numbers from the user and make the first number the exponent of the second number
#2- is x or y greater than 100,000? if greater, get the number again but if entered incorrectly, warn on the screen and get the number again
#3- check if the entered value is a number and negative but if entered incorrectly, warn on the screen and get the number again
#4- if a decimal value is entered, warn and get the number again but if entered incorrectly, warn on the screen and get the number again
#5- print the obtained result on the screen in a proper format. there should be a dot between the digits
#6- use a debugging mechanism in the program and control it with the hata_ayiklama variable 

import math

hata_ayiklama = True
MAX_DIGITS = 4300

def debug(message):
    if hata_ayiklama:
        print("[DEBUG]", message)

def get_number(message):
    while True:
        try:
            value = float(input(message))
            debug(f"Input as float: {value}")

            if not value.is_integer():
                print("Decimal number is not allowed.")
                continue

            value = int(value)
            debug(f"Converted to int: {value}")

            if value < 0:
                print("Negative number is not allowed.")
                continue

            if value > 100000:
                print("Number cannot be greater than 100.000")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")
            debug("Rejected: not a number")

# -------- MAIN PROGRAM --------

while True:
    exponent = get_number("Enter the exponent: ")
    base = get_number("Enter the base: ")

    if base == 0:
        digit_count = 1
    else:
        digit_count = int(exponent * math.log10(base)) + 1

    debug(f"Estimated digit count: {digit_count}")

    if digit_count > MAX_DIGITS:
        print("Result would be too large to display (over 4300 digits).")
        print("Please enter smaller numbers.\n")
        continue
    else:
        break

result = base ** exponent
formatted_result = f"{result:,}".replace(",", ".")
print("Result:", formatted_result)
