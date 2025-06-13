import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4."

    # Define character sets
    letters = string.ascii_letters  # A-Z + a-z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # !@#$%^&* etc.

    # Combine all characters
    all_chars = letters + digits + symbols

    # Ensure at least one from each category
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password
    password += random.choices(all_chars, k=length - 3)

    # Shuffle for randomness
    random.shuffle(password)

    return ''.join(password)

# Ask user for password length
try:
    user_length = int(input("🔢 Enter the desired password length: "))
    print("🔐 Generated Password:", generate_password(user_length))
except ValueError:
    print("❌ Please enter a valid number.")
