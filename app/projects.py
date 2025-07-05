import json
import os
from datetime import datetime

PROJECTS_FILE = "projects.json"

def create_project(user_email):
    print("\n=== Create New Project ===")
    title = input("Project Title: ")
    details = input("Project Details: ")
    target = input("Total Target (e.g. 250000): ")
    start_date = input("Start Date (YYYY-MM-DD): ")
    end_date = input("End Date (YYYY-MM-DD): ")

    project = {
        "owner": user_email,
        "title": title,
        "details": details,
        "target": target,
        "start_date": start_date,
        "end_date": end_date
    }

    if os.path.exists(PROJECTS_FILE):
        with open(PROJECTS_FILE, "r") as file:
            try:
                projects = json.load(file)
            except json.decoder.JSONDecodeError:
                projects = []
    else:
        projects = []

    projects.append(project)

    with open(PROJECTS_FILE, "w") as file:
        json.dump(projects, file, indent=4)

    print("✅ Project created successfully!")


def view_projects():
    print("\n=== All Projects ===")
    if not os.path.exists(PROJECTS_FILE):
        print("⚠️ No projects found.")
        return

    with open(PROJECTS_FILE, "r") as file:
        try:
            projects = json.load(file)
        except json.decoder.JSONDecodeError:
            print("⚠️ Projects file is empty or corrupted.")
            return

    if not projects:
        print("⚠️ No projects available.")
        return

    for idx, proj in enumerate(projects, start=1):
        print(f"\n📌 Project #{idx}")
        print(f"Title: {proj['title']}")
        print(f"Details: {proj['details']}")
        print(f"Target: {proj['target']} EGP")
        print(f"Start Date: {proj['start_date']}")
        print(f"End Date: {proj['end_date']}")
        print(f"Owner Email: {proj['owner']}")


def view_my_projects(user_email):
    print("\n=== My Projects ===")

    if not os.path.exists(PROJECTS_FILE):
        print("⚠️ No projects file found.")
        return

    with open(PROJECTS_FILE, "r") as file:
        try:
            projects = json.load(file)
        except json.decoder.JSONDecodeError:
            print("⚠️ Projects file is empty or corrupted.")
            return

    user_projects = [p for p in projects if p["owner"] == user_email]

    if not user_projects:
        print("⚠️ You don't have any projects.")
        return

    for idx, proj in enumerate(user_projects, start=1):
        print(f"\n📌 Project #{idx}")
        print(f"Title: {proj['title']}")
        print(f"Details: {proj['details']}")
        print(f"Target: {proj['target']} EGP")
        print(f"Start Date: {proj['start_date']}")
        print(f"End Date: {proj['end_date']}")


def edit_project(user_email):
    print("\n=== Edit Your Projects ===")

    if not os.path.exists(PROJECTS_FILE):
        print("⚠️ No projects file found.")
        return

    with open(PROJECTS_FILE, "r") as file:
        try:
            projects = json.load(file)
        except json.decoder.JSONDecodeError:
            print("⚠️ Projects file is empty or corrupted.")
            return

    user_projects = [p for p in projects if p["owner"] == user_email]

    if not user_projects:
        print("⚠️ You don't have any projects to edit.")
        return

    for idx, proj in enumerate(user_projects, start=1):
        print(f"\n{idx}. {proj['title']} ({proj['start_date']} to {proj['end_date']})")

    choice = input("\nEnter project number to edit (or press Enter to cancel): ")
    if choice == "":
        print("🟡 Edit cancelled.")
        return

    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(user_projects):
        print("❌ Invalid choice.")
        return

    proj_index = int(choice) - 1
    selected_proj = user_projects[proj_index]

    print("\nLeave blank to keep current value.\n")
    new_title = input(f"New Title [{selected_proj['title']}]: ") or selected_proj['title']
    new_details = input(f"New Details [{selected_proj['details']}]: ") or selected_proj['details']
    new_target = input(f"New Target [{selected_proj['target']}]: ") or selected_proj['target']
    new_start = input(f"New Start Date [{selected_proj['start_date']}]: ") or selected_proj['start_date']
    new_end = input(f"New End Date [{selected_proj['end_date']}]: ") or selected_proj['end_date']

    for p in projects:
        if p == selected_proj:
            p['title'] = new_title
            p['details'] = new_details
            p['target'] = new_target
            p['start_date'] = new_start
            p['end_date'] = new_end

    with open(PROJECTS_FILE, "w") as file:
        json.dump(projects, file, indent=4)

    print("✅ Project updated successfully!")


def delete_project(user_email):
    print("\n=== Delete Your Projects ===")

    if not os.path.exists(PROJECTS_FILE):
        print("⚠️ No projects file found.")
        return

    with open(PROJECTS_FILE, "r") as file:
        try:
            projects = json.load(file)
        except json.decoder.JSONDecodeError:
            print("⚠️ Projects file is empty or corrupted.")
            return

    user_projects = [p for p in projects if p["owner"] == user_email]

    if not user_projects:
        print("⚠️ You don't have any projects to delete.")
        return

    for idx, proj in enumerate(user_projects, start=1):
        print(f"\n{idx}. {proj['title']} ({proj['start_date']} to {proj['end_date']})")

    choice = input("\nEnter project number to delete (or press Enter to cancel): ")
    if choice == "":
        print("🟡 Deletion cancelled.")
        return

    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(user_projects):
        print("❌ Invalid choice.")
        return

    proj_index = int(choice) - 1
    selected_proj = user_projects[proj_index]

    confirm = input(f"⚠️ Are you sure you want to delete '{selected_proj['title']}'? (y/n): ").lower()
    if confirm != "y":
        print("🟡 Deletion cancelled.")
        return

    projects = [p for p in projects if p != selected_proj]

    with open(PROJECTS_FILE, "w") as file:
        json.dump(projects, file, indent=4)

    print("✅ Project deleted successfully!")


def search_projects_by_date():
    print("\n=== Search Projects by Date ===")

    if not os.path.exists(PROJECTS_FILE):
        print("⚠️ No projects file found.")
        return

    with open(PROJECTS_FILE, "r") as file:
        try:
            projects = json.load(file)
        except json.decoder.JSONDecodeError:
            print("⚠️ Projects file is empty or corrupted.")
            return

    if not projects:
        print("⚠️ No projects available.")
        return

    date_str = input("Enter a date (YYYY-MM-DD): ")
    try:
        search_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("❌ Invalid date format.")
        return

    found = False
    for proj in projects:
        try:
            start = datetime.strptime(proj['start_date'], "%Y-%m-%d").date()
            end = datetime.strptime(proj['end_date'], "%Y-%m-%d").date()
        except ValueError:
            continue

        if start <= search_date <= end:
            found = True
            print(f"\n📌 {proj['title']}")
            print(f"Details: {proj['details']}")
            print(f"Target: {proj['target']} EGP")
            print(f"Duration: {proj['start_date']} to {proj['end_date']}")
            print(f"Owner: {proj['owner']}")

    if not found:
        print("❌ No projects found for that date.")


def filter_projects_by_target():
    print("\n=== Filter Projects by Target ===")

    if not os.path.exists(PROJECTS_FILE):
        print("⚠️ No projects file found.")
        return

    with open(PROJECTS_FILE, "r") as file:
        try:
            projects = json.load(file)
        except json.decoder.JSONDecodeError:
            print("⚠️ Projects file is empty or corrupted.")
            return

    if not projects:
        print("⚠️ No projects available.")
        return

    min_target_str = input("Enter minimum target amount (EGP): ")
    min_target_cleaned = min_target_str.replace(',', '').strip()

    try:
        min_target = float(min_target_cleaned)
    except ValueError:
        print("❌ Invalid number.")
        return

    filtered = []
    for p in projects:
        try:
            project_target = float(str(p['target']).replace(',', '').strip())
            if project_target >= min_target:
                filtered.append(p)
        except ValueError:
            continue

    if not filtered:
        print(f"❌ No projects found with target >= {min_target} EGP.")
        return

    for idx, proj in enumerate(filtered, start=1):
        print(f"\n📌 Project #{idx}")
        print(f"Title: {proj['title']}")
        print(f"Details: {proj['details']}")
        print(f"Target: {proj['target']} EGP")
        print(f"Start Date: {proj['start_date']}")
        print(f"End Date: {proj['end_date']}")
        print(f"Owner: {proj['owner']}")
