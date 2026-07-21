# Random Passward Generator
# Password Strength Checker Module
import string
# Password Strength Checker
def check_strength(password):
    """
    Anlyze password strength.
        Weak,Medium, Strong, Very Strong
    """
    score = 0
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
# Length Check
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
# Character Checks
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_symbol = True
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1
    # Final Result
    if score <= 4:
        return "Weak"
    elif score <= 8:
        return "Medium"
    elif score <= 12:
        return "Strong"
    else:
        return "Very Strong"
# Testing
if __name__ == "__main__":
    while True:
        password = input("Enter Password: ")
        result = check_strength(password)
        print("Strength :", result)
        print("-" * 40)