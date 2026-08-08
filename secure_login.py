stored_username = "admin"
stored_password = "admin123"

username = input("Enter Username: ").strip()
password = input("Enter Password: ").strip()

if username == stored_username and password == stored_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")