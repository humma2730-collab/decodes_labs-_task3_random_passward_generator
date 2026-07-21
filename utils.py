# Random Passward Generator
# Utility Functions Module
import os
import platform
# Clear Screen
def clear_screen():
    """
    Clear terminal screen.
    Supports Windows and Linux/macOS.
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
# Pause Program
def pause():
    """
    Wait for user before continuing.
    """
    input("\nPress Enter to Continue...")
# Print Line
def print_line(length=60):
    print("*" * length)
def print_title(title):
    print_line()
    print(title.center(60))
    print_line()
# Welcome Banner
def banner():
    clear_screen()
    print("=" * 60)
    print("      ███████╗███████╗ ██████╗██╗   ██╗██████╗ ")
    print("      ██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗")
    print("      ███████╗█████╗  ██║     ██║   ██║██████╔╝")
    print("      ╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗")
    print("      ███████║███████╗╚██████╗╚██████╔╝██║  ██║")
    print("      ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝")
    print()
    print(" SECUREPASS PRO")
    print(" Advanced Password Generator")
    print("*" * 60)
# Validate Integer Input
def get_integer(message):
    while True:
        try:
            value = int(input(message))
            if value <= 0:
                print("Please enter a positive number.\n")
                continue
            return value
        except ValueError:
            print("Invalid Input! Numbers only.\n")
# Yes / No Input
def get_yes_no(message):
    while True:
        choice = input(message).strip().lower()
        if choice in ("y", "yes"):
            return True
        elif choice in ("n", "no"):
            return False
        else:
            print("Please enter Y or N.\n")
# Footer
def footer():
    print("\n" + "*" * 60)
    print("Thank You For Using Random Passward Generator !")
    print("=" * 60)
# Testing
if __name__ == "__main__":
    banner()
    length = get_integer("\nEnter Password Length : ")
    print("\nPassword Length :", length)
    upper = get_yes_no("Include Uppercase? (Y/N): ")
    print("Uppercase :", upper)
    pause()
    footer()