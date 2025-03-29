import re

def check_password_strength(password):
    # Define criteria for password strength
    min_length = 8
    max_length = 20
    has_upper = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'[@$!%*?&]', password) is not None
    length_valid = min_length <= len(password) <= max_length

    # Evaluate Password Strength
    strength = 0
    if length_valid:
        strength += 1
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    # Feedback based on strength
    if strength < 3:
        return "Weak Password: Consider adding uppercase letters, numbers, or special characters."
    elif strength == 3:
        return "Moderate Password: Good job! Consider making it stronger with more variety."
    else:
        return "Strong Password: Excellent choice!"

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    print(result)