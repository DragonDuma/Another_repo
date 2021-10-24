
username = input("Enter a Username:")
password = input("Enter a Password:")

print("You now have an account.")
print("Login:")

username2 = input("Enter Username:")
password2 = input("Enter Password:")

if username == username2 and password == password2:
    print("You have logged in successfully.")
else:
    print("Invalid Credentials")
