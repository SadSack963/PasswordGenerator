def pwd_gen_my_attempt():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91

    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    # Create array of allowed characters
    char_array = [letters, numbers, symbols]

    # Get last valid position in list
    last_letter = len(letters) - 1
    last_number = len(numbers) - 1
    last_symbol = len(symbols) - 1
    # List of last valid positions of character lists
    last_array = [last_letter, last_number, last_symbol]

    # Desired password length
    pwd_length = nr_letters + nr_numbers + nr_symbols

    # Initialize
    total_letters = 0
    total_numbers = 0
    total_symbols = 0
    pwd_final = ""

    # Weighting
    # Passwords are typically made up of
    #   many letters
    #   fewer numbers
    #   very few symbols
    # Weighting prevents the symbols and numbers being used up immediately
    # leaving a long string of letters at the end of the password
    letter_threshold = nr_letters / pwd_length
    number_threshold = letter_threshold + nr_numbers / pwd_length

    # Loop until password is complete
    for i in range(0, pwd_length):
        # Loop until a valid character is found
        done = False
        while not done:
            # Choose a random character type using the weighting
            #   0 = letter
            #   1 = number
            #   2 = symbol
            rand_float = random.random()
            if rand_float < letter_threshold:
                char_type = 0
            elif rand_float < number_threshold:
                char_type = 1
            else:
                char_type = 2

            # Check if there are still characters of this type required
            # If the current type is used up,
            # then done remains False and the while loop tries again
            if char_type == 0 and total_letters < nr_letters:
                total_letters += 1
                done = True
            if char_type == 1 and total_numbers < nr_numbers:
                total_numbers += 1
                done = True
            if char_type == 2 and total_symbols < nr_symbols:
                total_symbols += 1
                done = True

        # Choose a random character in the correct range
        rand_char = random.randint(0, last_array[char_type])

        # Add the selected character to the password
        pwd_final += (char_array[char_type][rand_char])

    print(f"Here is your password: {pwd_final}")