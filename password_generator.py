import random
import string

def generate_password(length):
    # Minimum length check
    if length < 4:
        print("Password length must be at least 4 characters.")
        return None

    # Character categories
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure at least one character from each category
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Fill the rest of the password length
    all_characters = uppercase + lowercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

def main():
    print("Welcome to the Random Password Generator!")
    try:
        length = int(input("Enter the desired password length (minimum 4): "))
        password = generate_password(length)
        if password:
            print(f"Your generated password is: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
