import random

answer = input("Input (yes/no):\n").lower()

while True:
    # Password 1: at least 5 letters
    while True:
        pw1 = input("1. Enter at least 5 letters:\n")
        if pw1.isalpha() and len(pw1) >= 5:
            break
        else:
            print("Error: Letters only and at least 5 characters!")

    # Password 2: exactly 1 digit
    while True:
        pw2 = input("2. Enter exactly one digit:\n")
        if pw2.isdigit() and len(pw2) == 1:
            break
        else:
            print("Error: Must be exactly one digit!")

    # Password 3: exactly 1 special character
    special_chars = [
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
        '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
        '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
    ]

    while True:
        pw3 = input("3. Enter a special character:\n")
        if pw3 in special_chars:
            break
        else:
            print("Error: Only special characters allowed!")

    # Password 4: one uppercase letter
    while True:
        pw4 = input("4. Enter one uppercase letter:\n")
        if pw4.isupper() and len(pw4) == 1:
            break
        else:
            print("Error: Only one uppercase letter!")

    # Password 5: a valid month
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        pw5 = input("5. Enter a month someone has a birthday in:\n").capitalize()
        if pw5 in months:
            break
        else:
            print("Error: Please enter a valid month!")

    # Password 6: first pet
    pets = [
        "Dog", "Cat", "Guinea pig", "Hamster", "Rabbit", "Budgie",
        "Parrot", "Fish", "Rat", "Mouse", "Chinchilla", "Hedgehog",
        "Ferret", "Turtle", "Iguana", "Snake", "Spider"
    ]

    while True:
        print(pets)
        pw6 = input("6. Enter your first pet:\n").capitalize()
        if pw6 in pets:
            break
        else:
            print("Error: Please enter a valid pet!")

    # Password 7: favorite color
    favorite_colors = [
        "Blue", "Red", "Green", "Yellow", "Purple", "Orange", "Black",
        "White", "Pink", "Turquoise", "Brown", "Gray", "Beige", "Violet", "Gold", "Silver"
    ]

    while True:
        print(favorite_colors)
        pw7 = input("7. Enter your favorite color:\n").capitalize()
        if pw7 in favorite_colors:
            break
        else:
            print("Error: Please enter a valid color!")

    # Password 8: two numbers that add up to 30
    while True:
        try:
            pw8_1 = int(input("8. Enter two numbers that add up to 30.\nFirst number:\n"))
            pw8_2 = int(input("Second number:\n"))
        except ValueError:
            print("Error: Numbers only!")
            continue

        if pw8_1 + pw8_2 == 30:
            break
        else:
            print("Error: The numbers must add up to 30!")

    # Password 9: brand
    brands = ["nike", "adidas", "puma"]
    while True:
        pw9 = input("9. Which of these brands fits you best? (nike, adidas, puma):\n").lower()
        if pw9 in brands:
            break
        else:
            print("Error: Only one of the 3 brands!")

    # Password 10: pick a random number
    while True:
        numbers = [random.randint(1, 100) for _ in range(3)]
        try:
            pw10 = int(input(f"10. Choose one of these random numbers: {numbers}\n"))
        except ValueError:
            print("Error: Numbers only!")
            continue

        if pw10 in numbers:
            break
        else:
            print("Error: Please choose one of the shown numbers!")

    # Final password output
    print(f"\n✅ Your final password: {pw1}{pw2}{pw3}{pw4}{pw5}{pw6}{pw7}{pw8_1}{pw8_2}{pw9}{pw10}")
    print("🎉 Password game completed!\n")

    # Play again?
    answer = input("Do you want to create another password? (yes/no):\n").lower()
    if answer != "yes":
        print("Program ended.")
        break
