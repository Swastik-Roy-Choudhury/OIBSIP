import random
import string

# Function to generate a random password
def generate_password(length, include_letters=True, include_digits=True, include_symbols=True):
    # Create a pool of characters based on user preferences
    character_pool = ''

    if include_letters:
        character_pool += string.ascii_letters  # Includes both lowercase and uppercase letters
    if include_digits:
        character_pool += string.digits         # Includes digits 0-9
    if include_symbols:
        character_pool += string.punctuation    # Includes special symbols (!, @, #, etc.)

    # Ensure that the character pool is not empty
    if not character_pool:
        raise ValueError("No character types selected! Please include at least one character type.")

    # Generate a random password from the pool
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

# Main function to get user preferences and generate the password
def password_generator():
    # Prompt user for password length and character preferences
    try:
        length = int(input("Enter the desired password length: "))
        include_letters = input("Include letters? (y/n): ").lower() == 'y'
        include_digits = input("Include digits? (y/n): ").lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        # Generate the password
        password = generate_password(length, include_letters, include_digits, include_symbols)

        # Display the generated password
        print(f"\nYour randomly generated password is: {password}")

    except ValueError:
        print("Invalid input. Please enter valid values for the password length and preferences.")

# Run the password generator
password_generator()
