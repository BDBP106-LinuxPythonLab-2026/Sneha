#Keep asking for a password until it meets all of these rules:
#at least 8 characters
#at least one uppercase letter, one lowercase letter and one digit
#at least one special character from {"!", "@", "#", "$", "%", "&", "*"}
#no spaces
#doesn't contain the word "password" in any case
#After each failed attempt, list every rule that was broken, not just the first one.

# Create a set containing all allowed special characters
# Keep asking for a password until a valid password is entered
    # Ask the user to enter a password
    # Create a flag to check for an uppercase letter
    # Create a flag to check for a lowercase letter
    # Create a flag to check for a digit
    # Create a flag to check for a special character
    # Create a flag to check for spaces
    # Go through every character in the password
        # Check if the character is an uppercase letter
        # Check if the character is a lowercase letter
        # Check if the character is a digit
        # Check if the character is one of the special characters
        # Check if the character is a space
    # Create an empty list to store all broken rules
    # Check if the password has fewer than 8 characters
    # Check if there is no uppercase letter
    # Check if there is no lowercase letter
    # Check if there is no digit
    # Check if there is no special character
    # Check if the password contains a space
    # Convert the password to lowercase and check for the word "password"
    # Check if there are no errors
        # Tell the user that the password is valid
        # Stop asking for passwords
    # If there are errors
        # Tell the user that the password is invalid
        # Go through every broken rule
            # Print each broken rule


special_characters = {"!", "@", "#", "$", "%", "&", "*"}

while True:
    password = input("Enter a password: ")

    # Flags
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_space = False

    # Check every character
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

        if char in special_characters:
            has_special = True

        if char == " ":
            has_space = True

    # Store all broken rules
    errors = []

    if len(password) < 8:
        errors.append("Password must have at least 8 characters.")

    if not has_upper:
        errors.append("Password must contain at least one uppercase letter.")

    if not has_lower:
        errors.append("Password must contain at least one lowercase letter.")

    if not has_digit:
        errors.append("Password must contain at least one digit.")

    if not has_special:
        errors.append("Password must contain at least one special character (!, @, #, $, %, &, *).")

    if has_space:
        errors.append("Password must not contain spaces.")

    if "password" in password.lower():
        errors.append("Password must not contain the word 'password'.")

    # Check whether any rules were broken
    if len(errors) == 0:
        print("Password is valid!")
        break
    else:
        print("Password is invalid. Rules broken:")
        for error in errors:
            print("-", error)