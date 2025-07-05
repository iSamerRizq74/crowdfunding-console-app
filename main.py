from app.auth import register_user, login_user
from app.projects import (
    create_project,
    view_projects,
    view_my_projects,
    edit_project,
    delete_project,
    search_projects_by_date,
    filter_projects_by_target
)


def main_menu():
    while True:
        print("\n=== CrowdFunding Console App ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            user_email = login_user()
            if user_email:
                project_menu(user_email)
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


def view_projects_menu(user_email):
    while True:
        print("\n=== View Projects ===")
        print("1. View All Projects")
        print("2. View My Projects")
        print("3. Back to Project Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_projects()
        elif choice == "2":
            view_my_projects(user_email)
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice. Try again.")


def project_menu(user_email):
    while True:
        print("\n=== Project Menu ===")
        print("1. Create Project")
        print("2. View Projects")
        print("3. Edit My Project")
        print("4. Delete My Project")
        print("5. Search Projects by Date")
        print("6. Filter Projects by Target")
        print("7. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_project(user_email)
        elif choice == "2":
            view_projects_menu(user_email)
        elif choice == "3":
            edit_project(user_email)
        elif choice == "4":
            delete_project(user_email)
        elif choice == "5":
            search_projects_by_date()
        elif choice == "6":
            filter_projects_by_target()
        elif choice == "7":
            print("🔓 Logged out.")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print(f"🔥 Error: {e}")
