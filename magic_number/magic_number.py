secret_number = 47
secret_number2 = 69

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input("Guess the secret number: "))

while number != secret_number:
    if number > secret_number:
        print("Ha ha! Your number is too high!")
        number = int(input("Guess the secret number: "))
    elif number < secret_number:
        print("Ha ha! Your number is too low!")
        number = int(input("Guess the secret number: "))
else:
    print("Well done, muggle! You are free now.")
