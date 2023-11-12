import random

def RandomPass(length):
    
    # Define character sets
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    digits = '1234567890'
    symbols = '@#$%_!'

    # Combine all character sets
    all_characters = uppercase + lowercase + digits + symbols

    password = (
        random.choice(uppercase) +
        random.choice(lowercase) +
        random.choice(digits) +
        random.choice(symbols) +
        ''.join(random.choice(all_characters) for _ in range(length - 4))
    )


    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)

    return shuffled_password

def NamePass(name):
    symbols = '@#$%_!'
    password = name + random.choice(symbols) + str(random.randint(1000, 9999))
    return password

# Note = You have to make a 'password.txt' file to save your password
def SaveToFile(password):
    with open("password.txt", "a") as file:
        file.write(password + "\n")


# Main 
print("Choose an option:")
print("1. Generate random password")
print("2. Generate password with your name")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    length = int(input("Enter the length of the random password: "))
    if length < 4:
        raise ValueError("Password length must be at least 4 characters for each character set")
    else:
        password = RandomPass(length)
        SaveToFile(password)
        print("Generated Password:", password)
        
        print("Password saved to password.txt")

elif choice == '2':
    name = input("Enter your name: ")
    password = NamePass(name)
    SaveToFile(password)
    print("Generated Password:", password)
    print("Password saved to password.txt")

else:
    print("Invalid choice. Please enter 1 or 2.")
