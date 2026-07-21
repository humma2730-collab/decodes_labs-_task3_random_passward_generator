# Random Passward Generator
# Passward Generator Module
import random
import string
# Generate Password Function
def generate_password(length,
                      uppercase=True,
                      lowercase=True,
                      numbers=True,
                      symbols=True):
    character_pool = ""
    password = []
# Add Selected Character Sets
    if uppercase:
        character_pool += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
    if lowercase:
        character_pool += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))
    if numbers:
        character_pool += string.digits
        password.append(random.choice(string.digits))
    if symbols:
        character_pool += string.punctuation
        password.append(random.choice(string.punctuation))
    # No option selected
    if character_pool == "":
        return None
    # Password length cannot be smaller
    # than selected character groups.
    if length < len(password):
        return None
# Fill Remaining Characters
    remaining = length - len(password)
    for _ in range(remaining):
        password.append(random.choice(character_pool))
 # Shuffle Passwod
    random.shuffle(password)
    return "".join(password)
# Testing
if __name__ == "__main__":
    print(generate_password(
        length=12,
        uppercase=True,
        lowercase=True,
        numbers=True,
        symbols=True
    ))