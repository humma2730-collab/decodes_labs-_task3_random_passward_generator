# Random Passward Generator
# File Manager Module
from datetime import datetime
import os
# File Name
FILE_NAME = "passwords.txt"
# Save Password
def save_password(password):
    try:
        current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        with open(FILE_NAME, "a") as file:
            file.write("=" * 60 + "\n")
            file.write(f"Date & Time : {current_time}\n")
            file.write(f"Password    : {password}\n")
            file.write("=" * 60 + "\n\n")
    except Exception as e:
        print("\nError Saving Password")
        print(e)
# View Saved Passwords
def view_passwords():
    try:
        if not os.path.exists(FILE_NAME):
            print("\nNo password history found.")
            return
        with open(FILE_NAME, "r") as file:
            data = file.read()
            if data.strip() == "":
                print("\nNo passwords saved yet.")
            else:
                print("\n")
                print("=" * 60)
                print(" SAVED PASSWORD HISTORY")
                print("=" * 60)
                print(data)
    except Exception as e:
        print("\nError Reading File")
        print(e)
# Delete Password History
def delete_history():
    try:
        if os.path.exists(FILE_NAME):
            open(FILE_NAME, "w").close()
            print("\nPassword History Deleted Successfully!")
        else:
            print("\nHistory File Not Found.")
    except Exception as e:
        print("\nSomething Went Wrong")
        print(e)
# Count Saved Passwords
def total_passwords():
    try:
        if not os.path.exists(FILE_NAME):
            return 0
        count = 0
        with open(FILE_NAME, "r") as file:
            for line in file:
                if line.startswith("Password"):
                    count += 1
        return count
    except:
        return 0
# Testing
if __name__ == "__main__":
    while True:
        print("\n *********FILE MANAGER TEST*********")
        print("1. Save Password")
        print("2. View Passwords")
        print("3. Delete History")
        print("4. Count Passwords")
        print("5. Exit")
        choice = input("\nChoose Option : ")
        if choice == "1":
            pwd = input("Enter Password : ")
            save_password(pwd)
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            delete_history()
        elif choice == "4":
            print("\nTotal Saved Passwords :", total_passwords())
        elif choice == "5":
            break
        else:
            print("\nInvalid Choice")