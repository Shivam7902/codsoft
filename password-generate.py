import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    
    if length < 4:
        print("Password length should be at least 4 characters.")
        return

  
    password = random.choices(all_characters, k=length)

    
    random.shuffle(password)

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
