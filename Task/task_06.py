# DevOps Login Authentication

# Problem : Create a simple login system.

# Conditions:
# Username = admin
# Password = devops123

# If both are correct: Print(Login Successful) Otherwise Print (Invalid Username or Password)

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "devops123":
    print("\nLogin Successful, Welcome",username,"!")
else:
    print("\nInvalid Username or Password!")