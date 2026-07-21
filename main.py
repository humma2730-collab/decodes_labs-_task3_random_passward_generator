# ******************************
# Random Passward Generator
# Advanced Password Generator
# Developed By: Huma Fatima
# ******************************
from generator import generate_password
from checker import check_strength
from file_manager import (
    save_password,
    view_passwords,
    delete_history,
    total_passwords
)
from utils import (
    banner,
    clear_screen,
    pause,
    get_integer,
    get_yes_no
)
# Menu
def show_menu():
    print("*" * 60)
    print(" SECUREPASS PRO")
    print(" Advanced Password Generator")
    print("*" * 60)
    print("1. Generate Password")
    print("2. Check Password Strength")
    print("3. View Saved Passwords")
    print("4. Delete Password History")
    print("5. Show Total Saved Passwords")
    print("6. Exit")
    print("*" * 60)
# Generate Password
def password_generator():
    clear_screen()
    print("*" * 60)
    print("PASSWORD GENERATOR")
    print("*" * 60)
    length = get_integer("Enter Password Length (Minimum 8): ")
    if length < 8:
        print("\nPassword must be at least 8 characters.")
        pause()
        return
    upper = get_yes_no("Include Uppercase Letters? (Y/N): ")
    lower = get_yes_no("Include Lowercase Letters? (Y/N): ")
    numbers = get_yes_no("Include Numbers? (Y/N): ")
    symbols = get_yes_no("Include Symbols? (Y/N): ")
    password = generate_password(
        length,
        upper,
        lower,
        numbers,
        symbols
    )
    if password is None:
        print("\nYou must select at least one character type.")
    else:
        print("\nGenerated Password")
        print("-" * 30)
        print(password)
        strength = check_strength(password)
        print("\nPassword Strength :", strength)
        save = get_yes_no("\nSave Password? (Y/N): ")
        if save:
            save_password(password)
            print("\nPassword Saved Successfully!")
    pause()
# Password Strength Checker
def strength_checker():
    clear_screen()
    print("*" * 60)
    print(" PASSWORD STRENGTH CHECKER")
    print("*" * 60)
    password = input("Enter Password : ")
    result = check_strength(password)
    print("\nPassword Strength :", result)
    pause()
# Main Function
def main():
    while True:
        banner()
        show_menu()
        choice = input("\nSelect Option : ")
        if choice == "1":
            password_generator()
        elif choice == "2":
            strength_checker()
        elif choice == "3":
            clear_screen()
            view_passwords()
            pause()
        elif choice == "4":
            clear_screen()
            delete_history()
            pause()
        elif choice == "5":
            clear_screen()
            print("*" * 60)
            print("TOTAL SAVED PASSWORDS")
            print("*" * 60)
            print("\nTotal Saved Passwords :", total_passwords())
            pause()
        elif choice == "6":
            print("\nThank You For Using SecurePass Pro.")
            break
        else:
            print("\nInvalid Choice!")
            pause()
# Program Starts Here
if __name__ == "__main__":
    main()