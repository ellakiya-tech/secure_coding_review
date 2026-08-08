# vulnerable_login.py
# Demonstration of an insecure login implementation.
# DO NOT use this approach in a real application.

USERNAME = "admin"
PASSWORD = "admin123"


def login():
    print("=== Vulnerable Login ===")

    username = input("Username: ")
    password = input("Password: ")

    # VULNERABILITY:
    # The password is stored and compared as plain text.
    if username == USERNAME and password == PASSWORD:
        print("Login successful!")
    else:
        print("Invalid username or password.")


if "_name_" == "_main_":
    login()