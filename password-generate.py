import random
import string

def generate_password(length):
    # Define character sets for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on desired complexity
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Check if the length is valid
    if length < 4:
        print("Password length should be at least 4 characters.")
        return

    # Generate a password by randomly selecting characters
    password = random.choices(all_characters, k=length)

    # Shuffle the characters to make it more random
    random.shuffle(password)

    # Convert the list of characters to a string
    password = ''.join(password)

    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)

        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
