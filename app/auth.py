import json
import os

USERS_FILE = "users.json"

def register_user():
    print("\n=== Register New User ===")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    password = input("Password: ")
    confirm_password = input("Confirm Password: ")
    phone = input("Phone (Egyptian only): ")

    if password != confirm_password:
        print("❌ Passwords do not match.")
        return

    user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone
    }

    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            try:
                users = json.load(file)
            except json.decoder.JSONDecodeError:
                users = []
    else:
        users = []

    if any(u["email"] == email for u in users):
        print("❌ Email already exists.")
        return

    users.append(user)

    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)

    print(f"✅ User {first_name} registered successfully!")

def login_user():
    print("\n=== Login ===")
    email = input("Email: ")
    password = input("Password: ")

    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            try:
                users = json.load(file)
            except json.decoder.JSONDecodeError:
                users = []
    else:
        users = []

    for user in users:
        if user["email"] == email and user["password"] == password:
            print(f"✅ Welcome back, {user['first_name']}!")
            return email  # ← رجع الإيميل هنا

    print("❌ Invalid email or password.")
    return None


