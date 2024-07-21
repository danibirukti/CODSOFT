import random
import string

def generate_password(length):
    # Define the character sets to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    # Prompt the user to specify the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("The length must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return

    # Generate the password
    password = generate_password(length)

    # Display the password
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
