import re

def check_password_strength(password):
    # Define criteria
    length_req = 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Calculate score based on criteria
    score = 0
    if len(password) >= length_req:
        score += 1
    if has_upper and has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    # Determine strength based on score
    if score == 4:
        return "Very Strong"
    elif score == 3:
        return "Strong"
    elif score == 2:
        return "Moderate"
    elif score == 1:
        return "Weak"
    else:
        return "Very Weak"

# Prompt the user to enter a password
def get_user_password():
    while True:
        password = input("Enter your password: ")
        strength = check_password_strength(password)
        print(f"Password strength: {strength}")
        
        # Optional: Add conditions for acceptable strength
        if strength == "Very Strong" or strength == "Strong":
            print("Password accepted.")
            break
        else:
            print("Password does not meet strength requirements. Please try again.\n")

# Call the function to get user input and check password strength
get_user_password()


